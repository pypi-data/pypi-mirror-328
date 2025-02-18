import argparse
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import sys
import os
import threading
import json
import yaml
import shutil

CONFIG_FILE_JSON = "beetmon.json"
CONFIG_FILE_YAML = "beetmon.yaml"
BEET_CONFIG_FILE = "beet.json"
BEET_CONFIG_YAML = "beet.yaml"

# Settings for high event rate detection
HIGH_EVENT_RATE_THRESHOLD = 10  # number of events in the last minute considered "high"
HIGH_EVENT_RATE_DELAY = 5         # override delay to 5 seconds if rate is high

class BuildHandler(FileSystemEventHandler):
    def __init__(self, watch_dirs, extensions, delay, script_config, base_path):
        """
        :param watch_dirs: list of directories (relative to base_path) to watch.
                           If set to ["."] then watch the entire project.
        :param extensions: list of file extensions to filter (if not empty).
        :param delay: debounce delay in seconds.
        :param script_config: dict with a beet config to temporarily replace the current one (or None).
        :param base_path: the project root directory.
        """
        self.watch_dirs = watch_dirs
        self.extensions = tuple(extensions)
        self.delay = delay
        self.script_config = script_config
        self.base_path = base_path
        self.build_scheduled = None
        self.lock = threading.Lock()
        self.event_timestamps = []  # to track event times (for high-rate detection)

    def dispatch(self, event):
        relative_path = os.path.relpath(event.src_path, self.base_path)
        start_level = relative_path.split(os.sep)[0]

        # Ignore changes to beet config files.
        if (self.script_config):
            if start_level.startswith('beet') and (start_level.endswith('.json') or start_level.endswith('.yaml')):
                return

        if self.watch_dirs != ["."]:
            if not any(relative_path.startswith(d) for d in self.watch_dirs):
                return
        else: #Default rule
            if start_level.startswith((".", "__")):
                return

        if self.extensions and not event.src_path.endswith(self.extensions):
            return

        super().dispatch(event)

    def on_modified(self, event):
        if event.is_directory:
            return

        now = time.time()
        with self.lock:
            self.event_timestamps.append(now)
            self.event_timestamps = [ts for ts in self.event_timestamps if now - ts <= 60]

            effective_delay = self.delay
            if self.delay < HIGH_EVENT_RATE_DELAY and len(self.event_timestamps) >= HIGH_EVENT_RATE_THRESHOLD:
                effective_delay = HIGH_EVENT_RATE_DELAY

            # Schedule beet build if not already scheduled.
            if self.build_scheduled is not None:
                self.build_scheduled.cancel()
            else:
                print(f"[beetmon] Changes detected. Running 'beet build' in {effective_delay} seconds...")

            self.build_scheduled = threading.Timer(effective_delay, self.run_build)
            self.build_scheduled.start()

    def run_build(self):
        with self.lock:
            self.build_scheduled = None
            #self.event_timestamps = []

        if not shutil.which("beet"):
            print("[beetmon] Error: 'beet' is not installed or not in PATH.")
            print("Install it via 'pip install beet'")
            sys.exit(1)

        #print("[beetmon] Running 'beet build'...")

        original_config = None
        if self.script_config:
            original_config = self.replace_beet_config(self.script_config)

        try:
            subprocess.run(["beet", "build"], check=True)
            #print("[beetmon] Build completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"[beetmon] Build failed: Status = {e.returncode}")
        finally:
            # Always restore (or remove) the temporary config if we applied a script config.
            if self.script_config:
                self.restore_beet_config(original_config)

    def replace_beet_config(self, script_config):
        """Back up the current beet config and replace it with the provided script config."""
        #print(f"script_config = {script_config}")
        
        backup_path = None

        if os.path.exists(BEET_CONFIG_FILE):
            backup_path = ".beet.json"
            shutil.move(BEET_CONFIG_FILE, backup_path)
        elif os.path.exists(BEET_CONFIG_YAML):
            backup_path = ".beet.yaml"
            shutil.move(BEET_CONFIG_YAML, backup_path)

        with open(BEET_CONFIG_FILE, "w") as f:
            json.dump(script_config, f, indent=2)

        return backup_path

    def restore_beet_config(self, backup_path):
        """Restore the original beet config after the build."""
        if os.path.exists(BEET_CONFIG_FILE):
            os.remove(BEET_CONFIG_FILE)
        if backup_path and os.path.exists(backup_path):
            shutil.move(backup_path, BEET_CONFIG_FILE if backup_path.endswith(".json") else BEET_CONFIG_YAML)


def load_config():
    """Load the beetmon config (JSON or YAML) and return as a dictionary."""
    config = {}
    if os.path.exists(CONFIG_FILE_JSON):
        with open(CONFIG_FILE_JSON, "r") as f:
            config = json.load(f)
    elif os.path.exists(CONFIG_FILE_YAML):
        with open(CONFIG_FILE_YAML, "r") as f:
            config = yaml.safe_load(f)
    return config

def standard_config_exists():
    return os.path.exists(BEET_CONFIG_FILE) or os.path.exists(BEET_CONFIG_YAML)

def select_script(config):
    """
    When no script is specified via CLI, choose the first available option from:
      1. Existing beet config file (beet.json or beet.yaml)
      2. "build" script
      3. "default" script
      4. Any script defined
    Returns the script name to use, or None if an existing beet config is found.
    """
    
    # Priority 1: Use existing beet config file if present.
    if standard_config_exists():
        return None

    # Otherwise, try to select one from the beetmon config's scripts.
    scripts = config.get("scripts", {})
    if not scripts:
        print("[beetmon] Error: No valid beet config found (and no scripts defined).")
        sys.exit(1)

    if "build" in scripts:
        return "build"
    elif "default" in scripts:
        return "default"
    else:
        return next(iter(scripts), None)

def main():
    if len(sys.argv) == 1 or sys.argv[1] not in ["init", "build"]:
        sys.argv.insert(1, "build")
    parser = argparse.ArgumentParser(description="Beetmon - Auto-build for Beet")
    subparsers = parser.add_subparsers(dest="command", required=True)
    init_parser = subparsers.add_parser("init", help="Initialize the Beetmon configuration")
    init_parser.set_defaults(func=handle_init)
    build_parser = subparsers.add_parser("build", help="Build a script from Beetmon config")
    build_parser.add_argument("script", nargs="?", help="Script name from Beetmon config")
    build_parser.add_argument("--delay", "--time", "-d", "-t", type=float,
                              help="Throttle time in seconds before triggering a build")
    build_parser.set_defaults(func=handle_build)
    args = parser.parse_args()
    args.func(args)

def handle_build(args):
    config = load_config()

    # Determine folders to watch. If no "watch" key is provided, default to watching the entire project.
    watch_dirs = config.get("watch", [])
    if not watch_dirs:
        watch_dirs = ["."]

    # Determine file extensions to filter.
    extensions = config.get("ext", "")
    extensions = [e.strip() for e in extensions.split(",") if e.strip()] if extensions else []

    # Use CLI delay if provided, else from config, defaulting to 2 seconds.
    delay = args.delay if args.delay is not None else config.get("delay", 2)

    script_name = args.script

    # If no script is specified via CLI, select one based on our priority.
    if standard_config_exists():
        print("[beetmon] Using existing beet config file.")
        if (script_name):
            print("[beetmon] Warning: Ignoring script name argument.")
        script_config = None
        script_override = False
    else:
        if script_name is None:
            script_name = select_script(config)
        script_config = config.get("scripts", {}).get(script_name) if script_name else None

        # If a script name was specified but not found in the config, error out.
        if script_name and script_config is None and config.get("scripts"):
            print(f"[beetmon] Error: Script '{script_name}' not found in beetmon config.")
            sys.exit(1)

        script_override = config.get("script_override", False)
        if (script_override and script_config is not None):
            script_config = {**(config.get("scripts", {}).get(select_script(config))),**(script_config)}

    base_path = os.getcwd()

    event_handler = BuildHandler(watch_dirs, extensions, delay, script_config, base_path)
    # Run an initial build.
    event_handler.run_build()

    observer = Observer()
    for directory in watch_dirs:
        observer.schedule(event_handler, os.path.join(base_path, directory), recursive=True)

    print(f"[beetmon] \x1b[35m Watching {watch_dirs} for changes... Press Ctrl+C to stop.\x1b[39m")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[beetmon] Stopped.")
    observer.join()

def handle_init(args):
    if (standard_config_exists() and not load_config()):
        try:
            is_json = True
            if os.path.exists(BEET_CONFIG_FILE):
                with open(BEET_CONFIG_FILE, "r") as file:
                    beet = json.load(file)
                os.remove(BEET_CONFIG_FILE)
            elif os.path.exists(BEET_CONFIG_YAML):
                with open(BEET_CONFIG_YAML, "r") as file:
                    beet = yaml.safe_load(file)
                os.remove(BEET_CONFIG_YAML)
                is_json = False
            config = {
                "watch": ["."],
                "ext": "",
                "delay": 3,
                "scripts": {"build": beet},
                "script_override": False
            }
            if is_json:
                with open(CONFIG_FILE_JSON, "w") as file:
                    json.dump(config, file, indent=2)
            else:
                with open(CONFIG_FILE_YAML, "w") as file:
                    yaml.dump(config, file)
                
        except Exception as e:
            print(f"[beetmon] Error initializing configuration: {e}")
    else:
        print("[beetmon] 'beetmon init' can't be executed: "+
              "beetmon config file already exists!" if standard_config_exists() else "beet config file not found!")
        print("Did you mean 'beetmon build init' instead?")


if __name__ == "__main__":
    main()
