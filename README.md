# OpenEduCat Student Verification Module

A comprehensive student verification module for OpenEduCat 18, designed to manage and verify high school student credentials and academic records.

**Developed by: Mostafa Hisham**  
**GitHub: [@Mostafa-Hisham0](https://github.com/Mostafa-Hisham0)**  
**Date: July 2024**

## 🎯 Features

- **Student Verification Management**: Create and manage student verification records
- **Academic Score Tracking**: Track total scores, maximum scores, and calculate percentages
- **Education System Support**: Support for various education systems (Thanaweya Amma, IGCSE, etc.)
- **Verification Workflow**: Pending, verified, and rejected status management
- **User Access Control**: Role-based access with proper security groups
- **Responsive UI**: Modern Odoo 18 interface with proper form and list views

## 🚀 Installation

### Prerequisites
- Odoo 18.0
- OpenEduCat 18.0
- Docker (recommended)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd openEduCat
   ```

2. **Start the Docker containers**
   ```bash
   docker-compose up -d
   ```

3. **Access Odoo**
   - URL: `http://localhost:8059`
   - Database: `HighSchools`
   - Username: `admin`
   - Password: `admin`

4. **Install the module**
   - Go to Apps → Search "Student Verification"
   - Click Install

## 📁 Module Structure

```
openeducat_student_verification/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── student_verification.py
├── views/
│   └── student_verification_view.xml
├── menus/
│   └── op_verification_menu.xml
├── security/
│   ├── op_verification_security.xml
│   └── ir.model.access.csv
└── data/
    └── verification_sequence.xml
```

## 🔧 Configuration

### Security Groups
- **Student Verification User**: Basic access to create and view records
- **Student Verification Manager**: Full access including verification actions
- **Student Verification Admin**: Complete administrative access

### Required Fields
- **Student**: Must be an existing student in the system
- **High School Name**: Name of the high school
- **Education System**: Type of education system
- **Graduation Year**: Year of graduation
- **Total Score**: Student's achieved score
- **Maximum Score**: Maximum possible score

### Computed Fields
- **Percentage**: Automatically calculated as (Total Score / Maximum Score) × 100
- **Verification Date**: Set automatically when verified
- **Verified By**: Set to current user when verified

## 🎨 Usage

### Creating a Verification Record
1. Navigate to **Student Verification** module
2. Click **Create** button
3. Fill in required fields:
   - Select a student
   - Enter high school name
   - Choose education system
   - Set graduation year
   - Enter total and maximum scores
4. Save the record

### Verification Process
1. Review the student information and scores
2. Click **Verify** button to approve
3. Or click **Reject** if verification fails
4. Add verification notes if needed

## 🔒 Security

The module implements proper access control:
- Users must be assigned to appropriate security groups
- Records are company-specific
- Audit trail for verification actions
- Data validation and constraints

## 🐛 Troubleshooting

### Common Issues

**Module not visible:**
- Ensure user is assigned to `base.group_user` group
- Check if module is installed and active

**Access denied errors:**
- Add user to appropriate verification security groups
- Verify company access rights

**Percentage calculation issues:**
- Ensure total score ≤ maximum score
- Check decimal precision settings

### Database Fixes

If you encounter data issues, run these scripts:

```python
# Add admin to verification groups
python add_admin_to_verification.py

# Fix percentage data
python fix_percentage_data.py
```

## 📊 Data Model

### Student Verification Model
```python
class StudentVerification(models.Model):
    _name = 'student.verification'
    _description = 'Student Verification'
    _order = 'create_date desc'
    
    # Core fields
    student = fields.Many2one('op.student', required=True)
    high_school_name = fields.Char(required=True)
    education_system = fields.Selection([...])
    graduation_year = fields.Integer(required=True)
    
    # Score fields
    total_score = fields.Float(required=True)
    maximum_score = fields.Float(required=True)
    percentage = fields.Float(compute='_compute_percentage', digits=(6, 2))
    
    # Status fields
    verification_status = fields.Selection([...])
    verification_date = fields.Datetime(readonly=True)
    verified_by = fields.Many2one('res.users', readonly=True)
    verification_notes = fields.Text()
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This module is part of the OpenEduCat ecosystem and follows the same licensing terms.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review Odoo and OpenEduCat documentation

## 🔄 Version History

- **v1.0.0**: Initial release with basic verification functionality
- **v1.1.0**: Added percentage calculation and validation
- **v1.2.0**: Improved security and access control
- **v1.3.0**: Enhanced UI and user experience

---

**Developed by Mostafa Hisham for OpenEduCat 18.0** 🎓

---

## 👨‍💻 **Developer Information**

- **Name:** Mostafa Hisham
- **GitHub:** [@Mostafa-Hisham0](https://github.com/Mostafa-Hisham0)
- **Email:** s-mostafa.ahmed@zewailcity.edu.eg
- **Project:** OpenEduCat Student Verification Module
- **Version:** 1.3.0
- **Development Date:** July 2024

**This module was developed as part of the OpenEduCat ecosystem to provide comprehensive student verification capabilities for educational institutions.**

