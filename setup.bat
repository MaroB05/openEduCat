@echo off
setlocal enabledelayedexpansion

echo 🚀 OpenEduCat Student Verification Module Setup
echo ================================================
echo.

:: Check if Docker is installed
echo [SETUP] Checking Docker installation...
docker --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not installed. Please install Docker Desktop first.
    pause
    exit /b 1
)
echo [INFO] Docker is installed

:: Check if Docker Compose is available
echo [SETUP] Checking Docker Compose...
docker compose version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker Compose is not available. Please install Docker Compose.
    pause
    exit /b 1
)
echo [INFO] Docker Compose is available

:: Create necessary directories
echo [SETUP] Creating necessary directories...
if not exist "sessions" mkdir sessions
if not exist "config" mkdir config
if not exist "addons" mkdir addons
echo [INFO] Directories created successfully

:: Check if odoo.conf exists
echo [SETUP] Checking Odoo configuration...
if not exist "config\odoo.conf" (
    echo [WARNING] odoo.conf not found. Creating basic configuration...
    (
        echo [options]
        echo admin_passwd = admin
        echo db_host = Odoo-DB
        echo db_port = 5432
        echo db_user = odoo
        echo db_password = odoo
        echo addons_path = /mnt/extra-addons
        echo data_dir = /var/lib/odoo
        echo logfile = /var/log/odoo/odoo.log
    ) > config\odoo.conf
    echo [INFO] Basic odoo.conf created
) else (
    echo [INFO] odoo.conf already exists
)

:: Check if compose.yaml exists
echo [SETUP] Checking Docker Compose configuration...
if not exist "compose.yaml" (
    if not exist "docker-compose.yml" (
        echo [WARNING] Docker Compose file not found. Creating basic configuration...
        (
            echo version: '3.8'
            echo.
            echo services:
            echo   Odoo-DB:
            echo     image: postgres:15
            echo     container_name: Odoo-DB
            echo     environment:
            echo       - POSTGRES_DB=postgres
            echo       - POSTGRES_PASSWORD=odoo
            echo       - POSTGRES_USER=odoo
            echo     volumes:
            echo       - postgres_data:/var/lib/postgresql/data
            echo     restart: unless-stopped
            echo.
            echo   Odoo:
            echo     image: odoo:18.0
            echo     container_name: Odoo
            echo     depends_on:
            echo       - Odoo-DB
            echo     ports:
            echo       - "8059:8069"
            echo     volumes:
            echo       - ./addons:/mnt/extra-addons
            echo       - ./config:/etc/odoo
            echo       - ./sessions:/var/lib/odoo/sessions
            echo     environment:
            echo       - HOST=Odoo-DB
            echo       - USER=odoo
            echo       - PASSWORD=odoo
            echo     restart: unless-stopped
            echo.
            echo volumes:
            echo   postgres_data:
        ) > compose.yaml
        echo [INFO] Basic compose.yaml created
    ) else (
        echo [INFO] docker-compose.yml already exists
    )
) else (
    echo [INFO] compose.yaml already exists
)

:: Ask user if they want to start services
set /p start_services="Do you want to start the services now? (y/n): "
if /i "%start_services%"=="y" (
    echo [SETUP] Starting Docker services...
    docker compose up -d
    if errorlevel 1 (
        echo [ERROR] Failed to start services
        pause
        exit /b 1
    )
    echo [INFO] Services started successfully
    
    echo [SETUP] Waiting for services to be ready...
    echo Waiting for PostgreSQL...
    timeout /t 10 /nobreak >nul
    echo Waiting for Odoo...
    timeout /t 20 /nobreak >nul
    echo [INFO] Services should be ready now
    
    echo.
    echo [SETUP] Access Information
    echo.
    echo 🌐 Odoo URL: http://localhost:8059
    echo 📊 Database: HighSchools (will be created on first access)
    echo 👤 Username: admin
    echo 🔑 Password: admin
    echo.
    echo 📁 Module Location: ./addons/openeducat_student_verification/
    echo.
    echo [WARNING] Remember to change the default passwords in production!
) else (
    echo [INFO] Setup completed. Run 'docker compose up -d' to start services.
)

echo.
echo [INFO] Setup completed successfully! 🎉
pause 