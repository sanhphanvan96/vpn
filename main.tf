provider "google" {
  project = "homelab-edge-20201205"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_project_service" "compute_engine_api" {
  service = "compute.googleapis.com"

  disable_dependent_services = true
  disable_on_destroy         = true
}

resource "google_compute_instance" "homelab_edge" {
  name         = "homelab-edge"
  machine_type = "f1-micro"

  boot_disk {
    initialize_params {
      image = "centos-8"
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }

  depends_on = [
    google_project_service.compute_engine_api
  ]
}