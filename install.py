import subprocess
import sys


def install_prerequisites():
    """Install prerequisites like curl and apt-transport-https."""
    print("Installing prerequisites (curl and apt-transport-https)...")
    subprocess.check_call(["sudo", "apt-get", "update"])
    subprocess.check_call(["sudo", "apt-get", "install", "-y", "curl", "apt-transport-https"])


def install_kubectl():
    """Install the kubectl command line tool."""
    print("Installing kubectl...")
    subprocess.check_call([
        "curl", "-LO",
        "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    ])
    subprocess.check_call(["chmod", "+x", "kubectl"])
    subprocess.check_call(["sudo", "mv", "kubectl", "/usr/local/bin/"])
    print("kubectl installed successfully!")


def install_minikube():
    """Install the minikube tool."""
    print("Installing Minikube...")
    subprocess.check_call(["curl", "-Lo", "minikube", "https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64"])
    subprocess.check_call(["chmod", "+x", "minikube"])
    subprocess.check_call(["sudo", "mv", "minikube", "/usr/local/bin/"])
    print("Minikube installed successfully!")


def start_minikube():
    """Start a Minikube Kubernetes cluster."""
    print("Starting Minikube...")
    subprocess.check_call(["minikube", "start"])
    print("Minikube started successfully!")


def main():
    """Main function to set up Kubernetes."""
    try:
        install_prerequisites()
        install_kubectl()
        install_minikube()
        start_minikube()
        print("Kubernetes setup completed successfully!")
    except subprocess.CalledProcessError as error:
        print(f"An error occurred while setting up Kubernetes: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()