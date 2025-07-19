# OpenEduCat 18 High School Student Verification Module - Testing and Debugging Guide

## Table of Contents
1. [Module Installation and Initial Setup](#1-module-installation-and-initial-setup)
2. [High School Management Testing](#2-high-school-management-testing)
3. [Student Application and Credential Capture Testing](#3-student-application-and-credential-capture-testing)
4. [Certificate Verification Workflow Testing](#4-certificate-verification-workflow-testing)
5. [User Interface and Reporting Testing](#5-user-interface-and-reporting-testing)
6. [Error Handling and Edge Cases](#6-error-handling-and-edge-cases)
7. [Debugging and Error Reporting](#7-debugging-and-error-reporting)
8. [Performance Testing](#8-performance-testing)
9. [Integration Testing](#9-integration-testing)

## 1. Module Installation and Initial Setup

### Objective
Verify that the module installs correctly and its basic configurations are accessible.

### Steps

#### 1.1 Module Installation
1. **Verify Module Location**: Ensure `openeducat_student_verification` is in your Odoo addons path
2. **Update Apps List**: Go to Apps → Update Apps List
3. **Install Module**: Search for "Student Verification" and install the module
4. **Check Dependencies**: Verify these modules are installed:
   - `openeducat_core`
   - `openeducat_admission`
   - `mail`
   - `web`

#### 1.2 Initial Configuration
1. **Access Configuration**: Navigate to Education → Configuration → Student Verification → Verification Configuration
2. **Verify Settings**: Check that all configuration options are present and editable
3. **Menu Verification**: Confirm these menu items are visible:
   - Education → Student Verification → High Schools
   - Education → Student Verification → Verification Records
   - Education → Student Verification → Verification Dashboard
   - Education → Student Verification → Reports

### Expected Outcome
- Module installs without errors
- All menu items are visible and functional
- Configuration settings are accessible
- Demo data loads correctly (if enabled)

### Test Data Available
The module includes comprehensive demo data:
- **Egyptian Schools**: Cairo International School, Alexandria Secondary School (Thanaweya Amma)
- **IGCSE Schools**: British International School Cairo, American International School in Egypt
- **American Diploma Schools**: Cairo American College, American School of Alexandria
- **Gulf Schools**: Dubai International Academy, Riyadh International School
- **Other Schools**: International School of Geneva

## 2. High School Management Testing

### Objective
Test the creation, modification, and retrieval of high school records.

### Scenarios

#### 2.1 Create New High Schools
**Test Case 1: Egyptian Thanaweya Amma School**
```
Steps:
1. Go to Education → Student Verification → High Schools → Create
2. Fill in the following data:
   - School Name: "Test Egyptian School"
   - Country: Egypt
   - City: Cairo
   - Education System: Thanaweya Amma (Egypt)
   - Accreditation Body: "Ministry of Education, Egypt"
   - Phone: "+20 2 1234 5678"
   - Email: "test@egyptianschool.edu.eg"
3. Save the record
4. Verify all fields are saved correctly
```

**Test Case 2: IGCSE School**
```
Steps:
1. Create a new high school with:
   - School Name: "Test IGCSE School"
   - Country: Egypt
   - Education System: IGCSE
   - Accreditation Body: "Cambridge Assessment International Education"
   - API Verification Enabled: ✓
2. Save and verify the record
```

**Test Case 3: American Diploma School**
```
Steps:
1. Create a new high school with:
   - School Name: "Test American School"
   - Country: Egypt
   - Education System: American Diploma
   - Accreditation Body: "AdvancED/Cognia"
   - API Verification Enabled: ✓
2. Save and verify the record
```

**Test Case 4: Gulf Country School**
```
Steps:
1. Create a new high school with:
   - School Name: "Test Gulf School"
   - Country: United Arab Emirates
   - City: Dubai
   - Education System: Gulf Country School
   - Accreditation Body: "Knowledge and Human Development Authority (KHDA)"
2. Save and verify the record
```

#### 2.2 Edit Existing High Schools
1. **Modify School Details**: Edit an existing school and change contact information
2. **Update Verification Status**: Use the "Verify School" and "Unverify School" buttons
3. **Test API Connection**: For schools with API verification enabled, test the API connection

#### 2.3 Search and Filter Functionality
1. **Search by Name**: Use the search bar to find schools by name
2. **Filter by Country**: Use the country filter to view schools by country
3. **Filter by Education System**: Filter schools by education system type
4. **Filter by Verification Status**: Filter by verified/unverified schools

### Expected Outcomes
- All high school records can be created, edited, and saved correctly
- Search and filter functions work properly
- Verification status changes are tracked
- API connection testing works (for enabled schools)
- Unique constraint prevents duplicate school names in the same country

## 3. Student Application and Credential Capture Testing

### Objective
Verify that student applications can be linked to high schools and credential fields are correctly captured.

### Scenarios

#### 3.1 New Student Application with Verification
**Test Case 1: Thanaweya Amma Student**
```
Steps:
1. Go to Education → Admission → Applications → Create
2. Fill in basic student information
3. In the "High School Verification" section:
   - Select High School: Choose a Thanaweya Amma school
   - High School Certificate Type: Should auto-populate to "Thanaweya Amma (Egypt)"
   - Graduation Year: Enter "2023"
   - Upload Certificate: Attach a sample certificate file
   - Upload Transcript: Attach a sample transcript file
4. Save the application
5. Verify all fields are saved correctly
```

**Test Case 2: IGCSE Student**
```
Steps:
1. Create a new application
2. Select an IGCSE high school
3. Verify certificate type auto-populates to "IGCSE"
4. Fill in graduation year and upload documents
5. Save and verify
```

**Test Case 3: American Diploma Student**
```
Steps:
1. Create a new application
2. Select an American Diploma high school
3. Verify certificate type auto-populates to "American Diploma"
4. Fill in graduation year and upload documents
5. Save and verify
```

#### 3.2 Existing Student Modification
1. **Update High School Information**: Modify an existing student's high school details
2. **Change Verification Status**: Update the verification status manually
3. **Add Verification Details**: Add notes in the verification details field

#### 3.3 Dynamic Field Behavior
1. **Certificate Type Auto-population**: Verify that selecting a high school auto-populates the certificate type
2. **Field Dependencies**: Test that required fields are enforced
3. **File Upload Validation**: Test uploading various file types and sizes

### Expected Outcomes
- Student applications correctly link to high schools
- Certificate type auto-populates based on selected high school
- All credential fields are accurately stored and displayed
- File uploads work correctly
- Validation rules are enforced

## 4. Certificate Verification Workflow Testing

### Objective
Test the various verification processes and status updates.

### Scenarios

#### 4.1 Manual Verification Process
**Test Case 1: Thanaweya Amma Verification**
```
Steps:
1. Create a student application with Thanaweya Amma credentials
2. Go to the application and click "Create Verification Record"
3. In the verification record:
   - Change verification status to "In Progress"
   - Add verification details: "Manual verification in progress"
   - Save the record
4. Update status to "Verified" or "Rejected"
5. Add detailed verification notes
6. Verify the status and notes are saved
```

#### 4.2 Automated Verification (Mock/Simulated)
**Test Case 2: IGCSE API Verification**
```
Steps:
1. Create a student application with IGCSE credentials
2. Create verification record
3. Test the verification workflow:
   - If API integration is implemented: Simulate API calls
   - If manual process: Record external verification results
4. Update verification status based on results
5. Add verification details with API response information
```

**Test Case 3: American Diploma Verification**
```
Steps:
1. Create a student application with American Diploma credentials
2. Create verification record
3. Test the verification workflow for external verification
4. Update status and add verification details
```

#### 4.3 Equivalency Calculation Testing
**Test Case 4: Score Calculation**
```
Steps:
1. For different certificate types, input sample grades/scores
2. Use the Equivalency Calculation Wizard:
   - Go to Education → Student Verification → Equivalency Calculation
   - Select certificate type and input grades
   - Calculate equivalent score
3. Verify calculations are accurate based on defined rules
4. Test edge cases (minimum scores, different grading scales)
```

#### 4.4 Bulk Verification Testing
**Test Case 5: Bulk Operations**
```
Steps:
1. Go to Education → Student Verification → Bulk Verification
2. Select multiple verification records
3. Test bulk status updates
4. Verify all selected records are updated correctly
```

### Expected Outcomes
- Verification workflow is smooth and intuitive
- Status updates are tracked correctly
- Verification details are saved and displayed
- Equivalency calculations are accurate
- Bulk operations work correctly
- API integration (if implemented) functions properly

## 5. User Interface and Reporting Testing

### Objective
Evaluate the usability of the module's interfaces and the accuracy of its reports.

### Scenarios

#### 5.1 High School Management Interface
1. **List View**: Verify all columns display correctly and sorting works
2. **Form View**: Check that all fields are properly laid out and accessible
3. **Search and Filter**: Test search functionality and filters
4. **Action Buttons**: Test "Verify School", "Unverify School", and "Test API Connection" buttons

#### 5.2 Student Application Interface
1. **Extended Form**: Verify the high school verification section is clearly visible
2. **Field Validation**: Test required field validation
3. **File Upload**: Test certificate and transcript upload functionality
4. **Verification Actions**: Test verification action buttons

#### 5.3 Verification Dashboard
1. **Dashboard Access**: Navigate to Education → Student Verification → Verification Dashboard
2. **Statistics Display**: Verify all statistics are displayed correctly
3. **Quick Actions**: Test quick action buttons
4. **Filtering**: Test dashboard filters and search

#### 5.4 Reports Testing
1. **Verification Status Report**: Generate and verify the verification status report
2. **Report Accuracy**: Check that report data matches actual records
3. **Export Functionality**: Test PDF and Excel export options
4. **Filtering**: Test report filters and date ranges

### Expected Outcomes
- All interfaces are intuitive and easy to navigate
- Forms display all required fields clearly
- Search and filter functions work properly
- Reports provide accurate and useful insights
- Export functionality works correctly

## 6. Error Handling and Edge Cases

### Objective
Identify and address unexpected behavior or errors.

### Scenarios

#### 6.1 Data Validation Testing
**Test Case 1: Required Fields**
```
Steps:
1. Try to save records with missing mandatory fields
2. Verify appropriate error messages are displayed
3. Test field-specific validation rules
```

**Test Case 2: Invalid Data Entry**
```
Steps:
1. Input invalid data types (e.g., text in number fields)
2. Test email format validation
3. Test phone number format validation
4. Verify validation error messages
```

#### 6.2 File Upload Testing
**Test Case 3: File Upload Validation**
```
Steps:
1. Test uploading various file types (PDF, JPG, DOC, etc.)
2. Test uploading large files
3. Test uploading files with special characters in names
4. Verify error handling for unsupported formats
```

#### 6.3 Security and Permissions Testing
**Test Case 4: Access Control**
```
Steps:
1. Test with different user roles:
   - Admissions Officer
   - Administrator
   - Regular User
2. Verify correct access controls are enforced
3. Test record creation, editing, and deletion permissions
```

#### 6.4 Edge Cases
**Test Case 5: Boundary Conditions**
```
Steps:
1. Test with very long school names
2. Test with special characters in text fields
3. Test with future graduation years
4. Test with very old graduation years
5. Test duplicate school names in different countries
```

### Expected Outcomes
- Module handles errors gracefully
- Clear error messages are displayed
- Security rules are enforced correctly
- File uploads are properly validated
- Edge cases are handled appropriately

## 7. Debugging and Error Reporting

### When Issues Occur

#### 7.1 Reproduce the Issue
1. **Document Steps**: Write down exact steps to reproduce the error
2. **Test Multiple Times**: Ensure the issue is consistent
3. **Note Environment**: Document browser, Odoo version, and user role

#### 7.2 Capture Evidence
1. **Screenshots**: Take screenshots of error messages and unexpected behavior
2. **Videos**: Record short videos of the issue (if helpful)
3. **Browser Console**: Check for JavaScript errors (F12 → Console tab)

#### 7.3 Check Odoo Logs
1. **Access Logs**: Check Odoo server logs for traceback errors
2. **Enable Debug Mode**: Enable debug mode to see detailed error information
3. **Log Location**: Typical locations:
   - Linux: `/var/log/odoo/odoo-server.log`
   - Windows: Check Odoo installation directory
   - Docker: `docker logs <container_name>`

#### 7.4 Common Error Types and Solutions

**Installation Errors**
```
Error: Module dependencies not met
Solution: Ensure all required modules are installed
- openeducat_core
- openeducat_admission
- mail
- web
```

**Permission Errors**
```
Error: Access denied to records
Solution: Check user permissions and access rights
- Verify user has proper access to student verification models
- Check security rules in ir.model.access.csv
```

**Validation Errors**
```
Error: Field validation failed
Solution: Check field constraints and validation rules
- Verify required fields are filled
- Check data format requirements
```

**File Upload Errors**
```
Error: File upload failed
Solution: Check file size and format restrictions
- Verify file size limits
- Check supported file formats
```

#### 7.5 Detailed Issue Report Template
When reporting issues, include:

```
**Issue Title**: Brief description of the problem

**Steps to Reproduce**:
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior**: What should happen

**Actual Behavior**: What actually happened

**Environment Details**:
- Odoo Version: [e.g., 18.0]
- OpenEduCat Version: [e.g., 18.0.1.0]
- Browser: [e.g., Chrome 120.0]
- Operating System: [e.g., Windows 10]

**Error Messages**: Exact error messages displayed

**Odoo Logs**: Relevant log entries (if any)

**Screenshots/Videos**: Attach relevant media

**Additional Notes**: Any other relevant information
```

## 8. Performance Testing

### Objective
Ensure the module performs well with large datasets.

### Scenarios

#### 8.1 Large Dataset Testing
1. **Multiple Schools**: Test with 100+ high school records
2. **Multiple Students**: Test with 1000+ student applications
3. **Verification Records**: Test with 500+ verification records

#### 8.2 Search Performance
1. **School Search**: Test search performance with large datasets
2. **Student Search**: Test student application search
3. **Verification Search**: Test verification record search

#### 8.3 Report Generation
1. **Large Reports**: Generate reports with large datasets
2. **Export Performance**: Test export performance for large reports

### Expected Outcomes
- Module performs acceptably with large datasets
- Search functions remain responsive
- Reports generate in reasonable time
- No memory leaks or performance degradation

## 9. Integration Testing

### Objective
Verify the module integrates properly with other OpenEduCat modules.

### Scenarios

#### 9.1 OpenEduCat Core Integration
1. **Student Records**: Verify integration with student management
2. **Admission Process**: Test integration with admission workflow
3. **User Management**: Test user permissions and access

#### 9.2 Mail Integration
1. **Notifications**: Test email notifications for verification status changes
2. **Activity Tracking**: Verify activity tracking works correctly

#### 9.3 Web Interface Integration
1. **UI Consistency**: Verify consistent UI with other modules
2. **Responsive Design**: Test mobile and tablet compatibility

### Expected Outcomes
- Module integrates seamlessly with other OpenEduCat modules
- Email notifications work correctly
- UI is consistent with the overall system
- No conflicts with existing functionality

## Conclusion

This comprehensive testing guide covers all major aspects of the OpenEduCat 18 High School Student Verification Module. By following these testing procedures, you can ensure the module functions correctly, handles various scenarios gracefully, and integrates seamlessly with the existing OpenEduCat system.

Remember to:
- Test thoroughly in a development environment before production deployment
- Document any issues found during testing
- Verify that all functionality works as expected
- Test with realistic data scenarios
- Ensure proper error handling and user feedback

For additional support or to report issues, refer to the OpenEduCat documentation or community forums. 