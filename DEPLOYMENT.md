# Deployment Guide - OpenEduCat Student Verification Module

This guide provides step-by-step instructions for deploying the OpenEduCat Student Verification Module in different environments.

## 🚀 Quick Deployment

### Option 1: Automated Setup (Recommended)

**For Linux/macOS:**
```bash
chmod +x setup.sh
./setup.sh
```

**For Windows:**
```cmd
setup.bat
```

### Option 2: Manual Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd openEduCat
   ```

2. **Start Docker services**
   ```bash
   docker compose up -d
   ```

3. **Access Odoo**
   - URL: `http://localhost:8059`
   - Create database: `HighSchools`
   - Username: `admin`
   - Password: `admin`

4. **Install the module**
   - Go to Apps → Search "Student Verification"
   - Click Install

## 🔧 Production Deployment

### Prerequisites
- Docker and Docker Compose
- Domain name (optional)
- SSL certificate (recommended)
- Backup strategy

### Security Configuration

1. **Change default passwords**
   ```bash
   # Edit config/odoo.conf
   admin_passwd = your_secure_master_password
   ```

2. **Update database credentials**
   ```yaml
   # In compose.yaml
   environment:
     - POSTGRES_PASSWORD=your_secure_db_password
   ```

3. **Enable SSL (recommended)**
   ```yaml
   # Add to compose.yaml
   ports:
     - "443:8069"  # HTTPS
   ```

### Environment Variables

Create a `.env` file:
```env
ODOO_MASTER_PASSWORD=your_secure_password
POSTGRES_PASSWORD=your_secure_db_password
ODOO_EMAIL=admin@yourdomain.com
ODOO_DOMAIN=yourdomain.com
```

### Backup Strategy

1. **Database backups**
   ```bash
   # Create backup script
   docker exec Odoo-DB pg_dump -U odoo HighSchools > backup_$(date +%Y%m%d_%H%M%S).sql
   ```

2. **File storage backups**
   ```bash
   # Backup addons and config
   tar -czf backup_$(date +%Y%m%d_%H%M%S).tar.gz addons/ config/
   ```

## 🌐 Cloud Deployment

### AWS Deployment

1. **EC2 Setup**
   ```bash
   # Install Docker on EC2
   sudo yum update -y
   sudo yum install -y docker
   sudo service docker start
   sudo usermod -a -G docker ec2-user
   ```

2. **Security Groups**
   - Allow port 8059 (or 443 for HTTPS)
   - Allow port 22 for SSH

3. **Deploy**
   ```bash
   git clone <your-repo-url>
   cd openEduCat
   docker compose up -d
   ```

### Azure Deployment

1. **Azure Container Instances**
   ```bash
   # Deploy using Azure CLI
   az container create \
     --resource-group myResourceGroup \
     --name odoo-container \
     --image odoo:18.0 \
     --ports 8069
   ```

### Google Cloud Platform

1. **Compute Engine**
   ```bash
   # Deploy on GCP
   gcloud compute instances create odoo-instance \
     --image-family ubuntu-2004-lts \
     --image-project ubuntu-os-cloud \
     --machine-type e2-medium
   ```

## 📊 Monitoring and Maintenance

### Health Checks

1. **Service status**
   ```bash
   docker compose ps
   docker compose logs -f
   ```

2. **Database health**
   ```bash
   docker exec Odoo-DB psql -U odoo -d HighSchools -c "SELECT version();"
   ```

### Performance Optimization

1. **Resource limits**
   ```yaml
   # In compose.yaml
   services:
     Odoo:
       deploy:
         resources:
           limits:
             memory: 2G
             cpus: '1.0'
   ```

2. **Database optimization**
   ```sql
   -- Regular maintenance
   VACUUM ANALYZE;
   REINDEX DATABASE HighSchools;
   ```

### Log Management

1. **Log rotation**
   ```yaml
   # Add to compose.yaml
   logging:
     driver: "json-file"
     options:
       max-size: "10m"
       max-file: "3"
   ```

2. **Centralized logging**
   ```yaml
   # For production
   logging:
     driver: "fluentd"
     options:
       fluentd-address: "localhost:24224"
   ```

## 🔄 Updates and Upgrades

### Module Updates

1. **Pull latest changes**
   ```bash
   git pull origin main
   ```

2. **Update module**
   ```bash
   docker exec -it Odoo odoo -d HighSchools -u openeducat_student_verification --stop-after-init
   ```

### Odoo Version Upgrades

1. **Backup first**
   ```bash
   docker exec Odoo-DB pg_dump -U odoo HighSchools > pre_upgrade_backup.sql
   ```

2. **Update image**
   ```yaml
   # In compose.yaml
   image: odoo:19.0  # New version
   ```

3. **Upgrade database**
   ```bash
   docker compose down
   docker compose up -d
   ```

## 🛠️ Troubleshooting

### Common Issues

**Service won't start:**
```bash
# Check logs
docker compose logs Odoo
docker compose logs Odoo-DB

# Check ports
netstat -tulpn | grep 8059
```

**Database connection issues:**
```bash
# Test database connection
docker exec Odoo-DB psql -U odoo -d postgres -c "\l"
```

**Module not visible:**
```bash
# Check module installation
docker exec -it Odoo odoo -d HighSchools --list-modules | grep verification
```

### Performance Issues

**High memory usage:**
```bash
# Check resource usage
docker stats

# Optimize Odoo settings
# Add to odoo.conf:
limit_memory_hard = 2684354560
limit_memory_soft = 2147483648
limit_request = 8192
limit_time_cpu = 600
limit_time_real = 1200
```

## 📞 Support

For deployment issues:
1. Check the troubleshooting section
2. Review Docker and Odoo logs
3. Create an issue on GitHub
4. Contact the development team

---

**Happy Deploying! 🚀** 