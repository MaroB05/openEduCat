# openEduCat Odoo Docker Setup

This repository contains a Dockerized setup for running **Odoo 18** with the **OpenEduCat** educational management modules. It simplifies deployment and makes it easier to contribute or customize the OpenEduCat platform.

---

## Project Structure

```
openEduCat/
├── addons/               # OpenEducat modules/addons
├── config/
│   └── odoo.conf         # Configuration file for Odoo
├── docker-compose.yaml   # Docker Compose file to set up Odoo and PostgreSQL
├── odoo_pg_pass          # File to store DB password
└── sessions/             # Volume for Odoo sessions
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MaroB05/openEduCat.git
cd openEduCat
```

### 2. Setup the Odoo Configuration

Edit the `config/odoo.conf` file with the following basic content:

```ini
[options]
addons_path = /mnt/extra-addons
data_dir = /var/lib/odoo
admin_passwd = your_master_password
db_host = db
db_port = 5432
db_user = odoo
db_password = odoo
```

> **Note:** Replace `your_master_password` with a secure value.

### 3. Start the Services

```bash
docker-compose up -d
```

This will start:

- `odoo`: The Odoo 18 application container
- `db`: A PostgreSQL container

Odoo will be accessible at:  
 http://localhost:8059

---

## 🧪 Verifying the Setup

You can monitor the logs using:

```bash
docker-compose logs -f
```

If everything is working, you should see logs from Odoo and PostgreSQL indicating successful startup.

---

## 🛠️ Useful Commands

| Task                          | Command                                     |
|-------------------------------|---------------------------------------------|
| Start services                | `docker-compose up -d`                      |
| Stop services                 | `docker-compose down`                       |
| Rebuild containers            | `docker-compose up --build --force-recreate`|
| View logs                     | `docker-compose logs -f`                    |
| Access Odoo container shell  | `docker exec -it odoo bash`                 |
| Access PostgreSQL shell       | `docker exec -it db psql -U odoo`           |

---

## 📚 OpenEduCat & Odoo Documentation

- **OpenEduCat Website:**  
  https://www.openeducat.org/

- **OpenEduCat Docs:**  
  https://docs.openeducat.org/

- **Odoo 18 Release Notes:**  
  https://www.odoo.com/odoo-18-release-notes

- **Odoo Developer Docs:**  
  https://www.odoo.com/documentation/18.0/developer.html

---

