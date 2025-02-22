import os
import json
from pathlib import Path

VERSION = "2.0.0"

# User config file location
USER_CONFIG_PATH = Path.home() / ".bourguibagpt" / "config.json"

# Default model configurations
MODEL_CONFIG = {
    "tiny": {
        "model_name": "gemma2:2b",
        "description": "Lightweight model suitable for systems with limited RAM",
        "ram_threshold": 6,
        "specs": {
            "min_ram": "4GB",
            "recommended_ram": "6GB",
            "disk_space": "2GB",
            "cpu": "2 cores"
        },
        "use_case": "Basic command-line tasks, simple queries"
    },
    "medium": {
        "model_name": "mistral-openorca:7b",
        "description": "Balanced model for systems with moderate RAM",
        "ram_threshold": 10,
        "specs": {
            "min_ram": "8GB",
            "recommended_ram": "12GB",
            "disk_space": "5GB",
            "cpu": "4 cores"
        },
        "use_case": "Complex commands, script generation"
    },
    "large": {
        "model_name": "phi4:14b",
        "description": "Full-size model for systems with ample RAM",
        "ram_threshold": 18,
        "specs": {
            "min_ram": "16GB",
            "recommended_ram": "24GB",
            "disk_space": "10GB",
            "cpu": "8 cores"
        },
        "use_case": "Advanced automation, detailed explanations"
    }
}

# OS-specific configurations
OS_CONFIG = {
    "Windows": {
        "install_cmd": "winget install Ollama.Ollama",
        "service_start": "net start ollama",
        "required_packages": ["winget"]
    },
    "Arch": {
        "install_cmd": "yay -S ollama",
        "service_start": "systemctl start ollama",
        "required_packages": ["yay"]
    },
    "Fedora": {
        "install_cmd": "sudo dnf install ollama",
        "service_start": "systemctl start ollama",
        "required_packages": ["dnf"]
    }
}

# Validation rules
VALIDATION_RULES = {
    "min_ram_gb": 4,
    "min_disk_gb": 2,
    "min_cpu_cores": 2
}

def get_recommended_model(available_ram_gb):
    """Returns the recommended model based on available RAM"""
    for model_size in ["tiny", "medium", "large"]:
        if available_ram_gb >= MODEL_CONFIG[model_size]["ram_threshold"]:
            return model_size
    return "tiny"  # Fallback to tiny if RAM is very limited

def save_user_config(model_choice: str) -> None:
    """Save user's model choice to config file"""
    os.makedirs(USER_CONFIG_PATH.parent, exist_ok=True)
    config = {"preferred_model": model_choice}
    with open(USER_CONFIG_PATH, 'w') as f:
        json.dump(config, f)

def load_user_config() -> str:
    """Load user's saved model choice"""
    if USER_CONFIG_PATH.exists():
        with open(USER_CONFIG_PATH) as f:
            config = json.load(f)
            return config.get("preferred_model")
    return None

def get_os_specific_config():
    """Get OS-specific configuration"""
    import platform
    system = platform.system()
    
    if system == "Linux":
        # Detect Linux distribution
        try:
            with open("/etc/os-release") as f:
                os_info = dict(line.strip().split('=', 1) for line in f if '=' in line)
            if "arch" in os_info.get("ID", "").lower():
                return OS_CONFIG["Arch"]
            elif "fedora" in os_info.get("ID", "").lower():
                return OS_CONFIG["Fedora"]
        except:
            pass
    elif system == "Windows":
        return OS_CONFIG["Windows"]
    
    return None