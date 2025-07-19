#!/bin/bash

# OpenEduCat Student Verification Module Setup Script
# This script helps you set up the module for development or production

set -e

echo "🚀 OpenEduCat Student Verification Module Setup"
echo "================================================"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_header() {
    echo -e "${BLUE}[SETUP]${NC} $1"
}

# Check if Docker is installed
check_docker() {
    print_header "Checking Docker installation..."
    if ! command -v docker &> /dev/null; then
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi
    print_status "Docker is installed"
}

# Check if Docker Compose is available
check_docker_compose() {
    print_header "Checking Docker Compose..."
    if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
        print_error "Docker Compose is not available. Please install Docker Compose."
        exit 1
    fi
    print_status "Docker Compose is available"
}

# Create necessary directories
create_directories() {
    print_header "Creating necessary directories..."
    
    mkdir -p sessions
    mkdir -p config
    mkdir -p addons
    
    print_status "Directories created successfully"
}

# Check if odoo.conf exists
check_config() {
    print_header "Checking Odoo configuration..."
    
    if [ ! -f "config/odoo.conf" ]; then
        print_warning "odoo.conf not found. Creating basic configuration..."
        cat > config/odoo.conf << EOF
[options]
admin_passwd = admin
db_host = Odoo-DB
db_port = 5432
db_user = odoo
db_password = odoo
addons_path = /mnt/extra-addons
data_dir = /var/lib/odoo
logfile = /var/log/odoo/odoo.log
EOF
        print_status "Basic odoo.conf created"
    else
        print_status "odoo.conf already exists"
    fi
}

# Check if docker-compose.yml exists
check_compose() {
    print_header "Checking Docker Compose configuration..."
    
    if [ ! -f "compose.yaml" ] && [ ! -f "docker-compose.yml" ]; then
        print_warning "Docker Compose file not found. Creating basic configuration..."
        cat > compose.yaml << EOF
version: '3.8'

services:
  Odoo-DB:
    image: postgres:15
    container_name: Odoo-DB
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_USER=odoo
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

  Odoo:
    image: odoo:18.0
    container_name: Odoo
    depends_on:
      - Odoo-DB
    ports:
      - "8059:8069"
    volumes:
      - ./addons:/mnt/extra-addons
      - ./config:/etc/odoo
      - ./sessions:/var/lib/odoo/sessions
    environment:
      - HOST=Odoo-DB
      - USER=odoo
      - PASSWORD=odoo
    restart: unless-stopped

volumes:
  postgres_data:
EOF
        print_status "Basic compose.yaml created"
    else
        print_status "Docker Compose file already exists"
    fi
}

# Start services
start_services() {
    print_header "Starting Docker services..."
    
    if command -v docker-compose &> /dev/null; then
        docker-compose up -d
    else
        docker compose up -d
    fi
    
    print_status "Services started successfully"
}

# Wait for services to be ready
wait_for_services() {
    print_header "Waiting for services to be ready..."
    
    echo "Waiting for PostgreSQL..."
    sleep 10
    
    echo "Waiting for Odoo..."
    sleep 20
    
    print_status "Services should be ready now"
}

# Display access information
show_access_info() {
    print_header "Access Information"
    echo ""
    echo "🌐 Odoo URL: http://localhost:8059"
    echo "📊 Database: HighSchools (will be created on first access)"
    echo "👤 Username: admin"
    echo "🔑 Password: admin"
    echo ""
    echo "📁 Module Location: ./addons/openeducat_student_verification/"
    echo ""
    print_warning "Remember to change the default passwords in production!"
}

# Main setup function
main() {
    print_header "Starting setup process..."
    
    check_docker
    check_docker_compose
    create_directories
    check_config
    check_compose
    
    read -p "Do you want to start the services now? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        start_services
        wait_for_services
        show_access_info
    else
        print_status "Setup completed. Run 'docker compose up -d' to start services."
    fi
    
    echo ""
    print_status "Setup completed successfully! 🎉"
}

# Run main function
main "$@" 