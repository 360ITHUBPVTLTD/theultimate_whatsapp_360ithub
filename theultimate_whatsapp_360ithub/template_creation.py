import frappe
import requests
from frappe import _
import json

import frappe
import json
import requests
from frappe import _

@frappe.whitelist()
def create_whatsapp_template(template_data):
    
    # Parse the JSON data sent from the client-side
    try:
        template_data = json.loads(template_data)
    except json.JSONDecodeError:
        frappe.throw(_("Invalid data format received. Expecting JSON."))

    # Fetch WhatsApp configuration (default and active filter)
    config = frappe.get_all(
        "WhatsApp Message Configuration",
        filters={},
        fields=['name', 'user_id', 'waba_number', 'wa_server', 'password', 'default', 'active']
    )

    if not config:
        frappe.throw(_("WhatsApp Message Configuration not found."))

    # Extract configuration details from the first record
    config = config[0]
    admin_settings = frappe.get_doc('WhatsApp Message Configuration', config.name)
    converted_password = admin_settings.get_password('password')

    # Check if config is either inactive or not set as default
    if not admin_settings.active or not admin_settings.default:
        if not admin_settings.active:
            return {"status": False, "msg": "WhatsApp instance is not active."}
        if not admin_settings.default:
            return {"status": False, "msg": "WhatsApp instance is not set as default."}

    # API URL
    api_url = f"{admin_settings.wa_server}/template"
    
    # Data to be sent as multipart/form-data
    payload = {
        "userid": config['user_id'],
        "password": converted_password,
        "wabaNumber": config['waba_number'],
        "output": (None, template_data.get("output")),
        "msgType": (None, template_data.get("msgType")),
        "header": (None, template_data.get("header")),
        "body": (None, template_data.get("body")),
        "footer": (None, template_data.get("footer")),
        "templateName": (None, template_data.get("templateName")),
        "docname": (None, template_data.get("docname")),
        "templateDescription": (None, template_data.get("templateDescription")),
        "language": (None, template_data.get("language")),
        "category": (None, template_data.get("category")),
    }

    headers = {
        "Content-Type": "multipart/form-data"  # Required for file uploads
    }

    try:
        # Make the request with form-data using `files` parameter
        response = requests.post(api_url, files=payload)
        response_data = response.json()

        # Check for success
        if response.status_code == 200:
            # Update the status field in the Text Template Creation doctype
            frappe.db.set_value('Text Template Creation', template_data['docname'], 'status', 'Pending')
            frappe.db.commit()  # Commit the changes
            
            return {
                "status": "success",
                "message": "Template created successfully. Status updated to 'Pending'."
            }
        else:
            return {
                "status": "error",
                "message": "Failed to create template. Status Code: {0}, Response: {1}".format(response.status_code, response.text)
            }

    except requests.exceptions.RequestException as e:
        frappe.throw(_("API request failed: {0}".format(str(e))))

######################################### SYnc template Status (Enabled or Disabled) ############################################

# import frappe
# import requests
# from frappe import _

# @frappe.whitelist()
# def sync_template_status():
#     # Get the WhatsApp API configuration (assuming there is a default entry)
#     config = frappe.get_all(
#         "WhatsApp Message Configuration",
#         filters={'default': 1},
#         fields=['name','user_id', 'waba_number', 'wa_server', 'password']
#     )

#     if not config:
#         frappe.throw(_("WhatsApp Message Configuration not found."))

#     # Extract configuration details from the first record
#     config = config[0]
#     admin_settings = frappe.get_doc('WhatsApp Message Configuration',config.name)
#     converted_passsword= admin_settings.get_password('password')
#     # print(converted_passsword)

#     if admin_settings.active == 0:
#         return {"status": False, "msg": "WhatsApp configuration is inactive."}
 
    
#     api_url_base = f"{config['wa_server']}/template"

#     # Get all the templates from the "Text Template Creation" doctype
#     templates = frappe.get_all("Text Template Creation",fields=["name", "template_name", "status"])

#     if not templates:
#         frappe.throw(_("No templates found which is having a status 'Pending'"))

#     # Loop through each template and call the API
#     for template in templates:
#         template_name = template.get("template_name")
#         if not template_name:
#             continue

#         api_url = f"{api_url_base}?userid={config['user_id']}&password={converted_passsword}&wabaNumber={config['waba_number']}&output=json&templateName={template_name}"
#         print(api_url)
#         try:
#             response = requests.get(api_url)
#             print(response.json())
#             if response.status_code == 200:
#                 data = response.json()

#                 if data.get("status") == "success" and data.get("templateList"):
#                     template_data = data["templateList"][0]

#                     whatsAppStatus = template_data["whatsAppStatus"]
#                     systemStatus = template_data["systemStatus"]

#                     # Update the template's status field based on the response
#                     if whatsAppStatus == "enabled" and systemStatus == "enabled":
#                         new_status = "Enabled"
#                     else:
#                         new_status = "Rejected"

#                     # Update the status in the "Text Template Creation" doctype
#                     frappe.db.set_value("Text Template Creation", template["name"], "status", new_status)

#             else:
#                 frappe.throw(_("Failed to sync template {0}. API returned status {1}".format(template_name, response.status_code)))

#         except requests.exceptions.RequestException as e:
#             frappe.throw(_("Failed to connect to the API for template {0}. Error: {1}".format(template_name, str(e))))

#     frappe.db.commit()  # Commit the changes after processing all templates
#     return "success"

import frappe
import requests
from frappe import _

@frappe.whitelist()
def sync_template_status():
    # Get the WhatsApp API configuration (assuming there is a default entry)
    config = frappe.get_all(
        "WhatsApp Message Configuration",
        filters={'default': 1,'active': 1},
        fields=['name','user_id', 'waba_number', 'wa_server', 'password']
    )

    if not config:
        frappe.throw(_("WhatsApp Message Configuration not found."))

    # Extract configuration details from the first record
    config = config[0]
    admin_settings = frappe.get_doc('WhatsApp Message Configuration', config.name)
    converted_password = admin_settings.get_password('password')

    if admin_settings.active == 0:
        return {"status": False, "msg": "WhatsApp configuration is inactive."}

    api_url_base = f"{config['wa_server']}/template"

    # Get all the templates from the "Text Template Creation" doctype
    templates = frappe.get_all("Text Template Creation", fields=["name", "template_name", "message_type", "status"])

    if not templates:
        frappe.throw(_("No templates found."))

    # Loop through each template and call the API
    for template in templates:
        template_name = template.get("template_name")
        message_type = template.get("message_type")

        if not template_name:
            continue

        api_url = f"{api_url_base}?userid={config['user_id']}&password={converted_password}&wabaNumber={config['waba_number']}&output=json&templateName={template_name}"
        print(api_url)

        try:
            response = requests.get(api_url)
            print(response.json())

            if response.status_code == 200:
                data = response.json()

                if data.get("status") == "success" and data.get("templateList"):
                    template_data = data["templateList"][0]

                    whatsAppStatus = template_data["whatsAppStatus"]
                    systemStatus = template_data["systemStatus"]

                    # Update the template's status field in "Text Template Creation"
                    if whatsAppStatus == "enabled" and systemStatus == "enabled":
                        new_status = "Enabled"
                    else:
                        new_status = "Rejected"

                    # Update the status in "Text Template Creation"
                    frappe.db.set_value("Text Template Creation", template["name"], "status", new_status)

                    # If the template is enabled, insert it into "WhatsApp Templates"
                    if new_status == "Enabled":
                        # Check if the template already exists in "WhatsApp Templates"
                        existing_template = frappe.db.exists("WhatsApp Templates", {"template_name": template_name})

                        if not existing_template:
                            # Insert the template into "WhatsApp Templates"
                            new_template = frappe.get_doc({
                                "doctype": "WhatsApp Templates",
                                "template_name": template_name,
                                "message_type": message_type
                            })
                            new_template.insert(ignore_permissions=True)
                            frappe.db.commit()  # Commit the transaction after inserting
                            print(f"Inserted template: {template_name}")
                        else:
                            print(f"Template {template_name} already exists in WhatsApp Templates.")

            else:
                frappe.throw(_("Failed to sync template {0}. API returned status {1}".format(template_name, response.status_code)))

        except requests.exceptions.RequestException as e:
            frappe.throw(_("Failed to connect to the API for template {0}. Error: {1}".format(template_name, str(e))))

    return "success"
