# import frappe
# import requests

# @frappe.whitelist()
# def bulk_send_whatsapp_messages():
#     # Fetch all documents with the "mobile" field from the "Bulk WhatsApp" doctype
#     bulk_whatsapp_docs = frappe.get_all("Bulk WhatsApp", filters={}, fields=["mobile"])
#     print("numbers fetched:", bulk_whatsapp_docs)

#     if not bulk_whatsapp_docs:
#         return {"status": False, "msg": "No mobile numbers found."}

#     # Prepare the list of mobile numbers from the fetched docs
#     mobile_numbers = [doc.mobile for doc in bulk_whatsapp_docs if doc.mobile]
#     print("mobile numbers:", mobile_numbers)
    
#     if not mobile_numbers:
#         return {"status": False, "msg": "No valid mobile numbers found."}

#     # Define the API endpoint and headers
#     url = "https://theultimate.io/WAApi/send"
#     headers = {
#         "apikey": "885a1a2e9946593fa38dc230b7975c17bff30a7a",
#         "Content-Type": "application/json"
#     }

#     # Define the common data (message content, etc.)
#     # Add the actual message content here
#     # dynamic_message = "Good morning! This is your bulk message."
#     common_data = {
#         "userid": "visionselfwa",
#         # "msg": dynamic_message,  # Add the message content here
#         "wabaNumber": "918792765755",
#         "output": "json",
#         "sendMethod": "quick",
#         "msgType": "text",
#         "templateName": "utility_templateto_send_bulk_text_message",  # Ensure this template exists
#     }

#     # Track message sending status
#     success_count = 0
#     failure_count = 0

#     # Loop through each mobile number and send the message
#     for mobile in mobile_numbers:
#         # if mobile != "919098543046":
#         #     continue
#         data = common_data.copy()  # Use common data and update mobile
        
#         data["mobile"] = mobile
        
#         # Send the POST request to WhatsApp API
#         response = requests.post(url, headers=headers, json=data)

#         # Log the response for debugging
#         print(f"Response for {mobile}: {response.status_code}, {response.text}")
        
#         # Try parsing the response to see if it's JSON
#         try:
#             response_data = response.json()
#             # Log parsed response data
#             print(f"Parsed Response for {mobile}: {response_data}")
            
#             # Check if the message was sent successfully based on actual response data
#             if response.status_code == 200 and response_data.get('status') == "success":
#                 success_count += 1
#             else:
#                 failure_count += 1
#         except Exception as e:
#             print(f"Error parsing response for {mobile}: {str(e)}")
#             failure_count += 1

#     return {
#         "status": True if success_count > 0 else False,
#         "msg": f"Messages sent: {success_count}, Failed: {failure_count}"
#     }


################################ Bulk sending Media(PDF) Message ##############################

# import frappe
# import requests

# @frappe.whitelist()
# def bulk_send_whatsapp_media():
#     # Fetch all documents with the "mobile" field from the "Bulk WhatsApp" doctype
#     bulk_whatsapp_docs = frappe.get_all("Bulk WhatsApp", filters={}, fields=["mobile"])
#     print("numbers fetched:", bulk_whatsapp_docs)

#     if not bulk_whatsapp_docs:
#         return {"status": False, "msg": "No mobile numbers found."}

#     # Prepare the list of mobile numbers from the fetched docs
#     mobile_numbers = [doc.mobile for doc in bulk_whatsapp_docs if doc.mobile]
#     print("mobile numbers:", mobile_numbers)
    
#     if not mobile_numbers:
#         return {"status": False, "msg": "No valid mobile numbers found."}

#     # Define the API endpoint and headers
#     url = "https://theultimate.io/WAApi/send"
#     headers = {
#         "apikey": "885a1a2e9946593fa38dc230b7975c17bff30a7a",
#         "Content-Type": "application/json"
#     }

#     # Define the common data for sending media (PDF document in this case)
#     common_data = {
#         "userid": "visionselfwa",
#         "wabaNumber": "918792765755",
#         "output": "json",
#         "sendMethod": "quick",
#         "msgType": "media",
#         "templateName": "utility_templateto_send_bulk_pdf_message",  # Ensure this template exists on your server
#         "mediaType": "document",  # This can be document, image, etc.
#         "mediaId": "5548960402374279504",  # Media ID of the uploaded document on WhatsApp's server
#         "documentName": "This is Dummy PDF.pdf",  # Name of the document being sent
#     }

#     # Track media sending status
#     success_count = 0
#     failure_count = 0

#     # Loop through each mobile number and send the media file
#     for mobile in mobile_numbers:
#         data = common_data.copy()  # Use common data and update mobile
#         data["mobile"] = mobile
        
#         # Send the POST request to WhatsApp API
#         response = requests.post(url, headers=headers, json=data)

#         # Log the response for debugging
#         print(f"Response for {mobile}: {response.status_code}, {response.text}")
        
#         # Try parsing the response to see if it's JSON
#         try:
#             response_data = response.json()
#             # Log parsed response data
#             print(f"Parsed Response for {mobile}: {response_data}")
            
#             # Check if the message was sent successfully based on actual response data
#             if response.status_code == 200 and response_data.get('status') == "success":
#                 success_count += 1
#             else:
#                 failure_count += 1
#         except Exception as e:
#             print(f"Error parsing response for {mobile}: {str(e)}")
#             failure_count += 1

#     return {
#         "status": True if success_count > 0 else False,
#         "msg": f"Media sent: {success_count}, Failed: {failure_count}"
#     }




###############################  Bulk sending Image Message #####################################

# import frappe
# import requests

# @frappe.whitelist()
# def bulk_send_whatsapp_images():
#     # Fetch all documents with the "mobile" field from the "Bulk WhatsApp" doctype
#     bulk_whatsapp_docs = frappe.get_all("Bulk WhatsApp", filters={}, fields=["mobile"])
#     print("Numbers fetched:", bulk_whatsapp_docs)

#     if not bulk_whatsapp_docs:
#         return {"status": False, "msg": "No mobile numbers found."}

#     # Prepare the list of mobile numbers from the fetched docs
#     mobile_numbers = [doc.mobile for doc in bulk_whatsapp_docs if doc.mobile]
#     print("Mobile numbers:", mobile_numbers)
    
#     if not mobile_numbers:
#         return {"status": False, "msg": "No valid mobile numbers found."}

#     # Define the API endpoint and headers
#     url = "https://theultimate.io/WAApi/send"
#     headers = {
#         "apikey": "885a1a2e9946593fa38dc230b7975c17bff30a7a",
#         "Content-Type": "application/json"
#     }

#     # Define the common data for sending images
#     common_data = {
#         "userid": "visionselfwa",
#         "wabaNumber": "918792765755",
#         "output": "json",
#         "sendMethod": "quick",
#         "msgType": "media",
#         "templateName": "template_having_media_with_image",  # Ensure this template exists
#         "mediaType": "image",  # Media type for images
#         "mediaId": "7358866669387402708",  # Media ID of the uploaded image on WhatsApp's server
#     }

#     # Track media sending status
#     success_count = 0
#     failure_count = 0

#     # Loop through each mobile number and send the image
#     for mobile in mobile_numbers:
#         data = common_data.copy()  # Use common data and update mobile
#         data["mobile"] = mobile
        
#         # Send the POST request to WhatsApp API
#         response = requests.post(url, headers=headers, json=data)

#         # Log the response for debugging
#         print(f"Response for {mobile}: {response.status_code}, {response.text}")
        
#         # Try parsing the response to see if it's JSON
#         try:
#             response_data = response.json()
#             # Log parsed response data
#             print(f"Parsed Response for {mobile}: {response_data}")
            
#             # Check if the message was sent successfully based on actual response data
#             if response.status_code == 200 and response_data.get('status') == "success":
#                 success_count += 1
#             else:
#                 failure_count += 1
#         except Exception as e:
#             print(f"Error parsing response for {mobile}: {str(e)}")
#             failure_count += 1

#     return {
#         "status": True if success_count > 0 else False,
#         "msg": f"Images sent: {success_count}, Failed: {failure_count}"
#     }


######################## Below code is dynamically generated everything to send a PDF #################################

# import frappe
# import requests

# @frappe.whitelist()
# def bulk_send_whatsapp_media(template_name):
#     print("Template Name:", template_name)
#     # Fetch the WhatsApp configuration with default set to 1
#     config = frappe.get_all(
#         "WhatsApp Message Configuration",
#         filters={'default': 1},
#         fields=['name', 'user_id', 'waba_number', 'wa_server', 'output', 'api_key', 'password']
#     )
    
#     # Check if configuration is available
#     if not config:
#         return {"status": False, "msg": "WhatsApp configuration not found."}
    
#     # Extract the first (and assumed only) configuration since get_all returns a list
#     config_doc = config[0]  # Get the first item from the list
#     admin_settings = frappe.get_doc('WhatsApp Message Configuration', config_doc['name'])  # Use config_doc['name']
#     converted_api_key = admin_settings.get_password('api_key')
#     print(converted_api_key)
    
#     # Fetch all documents with the "mobile" field from the "Bulk WhatsApp" doctype
#     bulk_whatsapp_docs = frappe.get_all("Bulk WhatsApp", filters={}, fields=["mobile","last_name","amount"])
#     print("Numbers fetched:", bulk_whatsapp_docs)

#     if not bulk_whatsapp_docs:
#         return {"status": False, "msg": "No mobile numbers found."}

#     # Prepare the list of mobile numbers from the fetched docs
#     mobile_numbers = [doc['mobile'] for doc in bulk_whatsapp_docs if doc['mobile']]
#     print("Mobile numbers:", mobile_numbers)
    
#     if not mobile_numbers:
#         return {"status": False, "msg": "No valid mobile numbers found."}

#     # Fetch the template details
#     template_doc = frappe.get_doc("WhatsApp Templates", template_name)
    
#     if not template_doc:
#         return {"status": False, "msg": "Template not found."}

#     # Define the API endpoint and headers
#     url = f"{config_doc['wa_server']}/send"
#     headers = {
#         "apikey": converted_api_key,  # Fetching API key dynamically
#         "Content-Type": "application/json"
#     }

    

#     # Define the common data for sending media
#     common_data = {
#         "userid": config_doc['user_id'],  # Fetch user ID dynamically
#         "wabaNumber": config_doc['waba_number'],  # Fetch WABA number dynamically
#         "output": config_doc['output'],  # Fetch output format dynamically
        
#         "sendMethod": template_doc.send_method,  # Use the template's send method
#         "msgType": template_doc.message_type,  # Use the template's message type
#         "templateName": template_doc.template_name,  # Name of the document being sent
#         # "mediaUrl": template_doc.media_url,  # Use the template's media URL
#         "mediaType": template_doc.media_type,  # Use the template's media type      
#     }

#     # Track media sending status
#     success_count = 0
#     failure_count = 0

#     # Loop through each mobile number and send the media file
#     for mobile in mobile_numbers:
#         data = common_data.copy()  # Use common data and update mobile
#         data["mobile"] = mobile
        
#         # Send the POST request to WhatsApp API
#         response = requests.post(url, headers=headers, json=data)

#         # Log the response for debugging
#         print(f"Response for {mobile}: {response.status_code}, {response.text}")
        
#         # Try parsing the response to see if it's JSON
#         try:
#             response_data = response.json()
#             # Log parsed response data
#             print(f"Parsed Response for {mobile}: {response_data}")
            
#             # Check if the message was sent successfully based on actual response data
#             if response.status_code == 200 and response_data.get('status') == "success":
#                 success_count += 1
#             else:
#                 failure_count += 1
#         except Exception as e:
#             print(f"Error parsing response for {mobile}: {str(e)}")
#             failure_count += 1

#     return {
#         "status": True if success_count > 0 else False,
#         "msg": f"Media sent: {success_count}, Failed: {failure_count}"
#     }


################################ Below code is having the variables in the whatsApp message #################################

# import frappe
# import requests

# @frappe.whitelist()
# def bulk_send_whatsapp_media(template_name):
#     print("Template Name:", template_name)
#     # Fetch the WhatsApp configuration with default set to 1
#     config = frappe.get_all(
#         "WhatsApp Message Configuration",
#         filters={'default': 1},
#         fields=['name', 'user_id', 'waba_number', 'wa_server', 'output', 'api_key', 'password']
#     )
    
#     # Check if configuration is available
#     if not config:
#         return {"status": False, "msg": "WhatsApp configuration not found."}
    
#     # Extract the first (and assumed only) configuration since get_all returns a list
#     config_doc = config[0]
#     admin_settings = frappe.get_doc('WhatsApp Message Configuration', config_doc['name'])
#     converted_api_key = admin_settings.get_password('api_key')
#     print(converted_api_key)
    
#     # Fetch all documents with the "mobile", "last_name", and "amount" fields from the "Bulk WhatsApp" doctype
#     bulk_whatsapp_docs = frappe.get_all("Bulk WhatsApp", filters={}, fields=["mobile", "last_name", "amount"])
#     print("Numbers fetched:", bulk_whatsapp_docs)

#     if not bulk_whatsapp_docs:
#         return {"status": False, "msg": "No mobile numbers found."}

#     # Prepare the list of mobile numbers from the fetched docs
#     mobile_numbers = [doc['mobile'] for doc in bulk_whatsapp_docs if doc['mobile']]
#     print("Mobile numbers:", mobile_numbers)
    
#     if not mobile_numbers:
#         return {"status": False, "msg": "No valid mobile numbers found."}

#     # Fetch the template details
#     template_doc = frappe.get_doc("WhatsApp Templates", template_name)
    
#     if not template_doc:
#         return {"status": False, "msg": "Template not found."}

#     # Define the API endpoint and headers
#     url = f"{config_doc['wa_server']}/send"
#     headers = {
#         "apikey": converted_api_key,  # Fetching API key dynamically
#         "Content-Type": "application/json"
#     }

#     # Define the common data for sending media
#     common_data = {
#         "userid": config_doc['user_id'],  # Fetch user ID dynamically
#         "wabaNumber": config_doc['waba_number'],  # Fetch WABA number dynamically
#         "output": config_doc['output'],  # Fetch output format dynamically
#         "sendMethod": template_doc.send_method,  # Use the template's send method
#         "msgType": template_doc.message_type,  # Use the template's message type
#         "templateName": template_doc.template_name,  # Name of the document being sent
#         "mediaUrl": template_doc.media_url,  # Use the template's media URL
#         "mediaType": template_doc.media_type,  # Use the template's media type
#     }

#     # Track media sending status
#     success_count = 0
#     failure_count = 0

#     # Loop through each mobile number and send the media file with a customized message
#     for doc in bulk_whatsapp_docs:
#         mobile = doc['mobile']
#         last_name = doc['last_name']
#         amount = doc['amount']

#         # Prepare the dynamic message
#         message = f"Dear Customer,\nYour name is {last_name}\nYour Invoice amount is {amount}"

#         # Copy the common data and add the mobile number and the customized message
#         data = common_data.copy()
#         data["mobile"] = mobile
#         data["msg"] = message  # Add the dynamic message

#         # Send the POST request to WhatsApp API
#         response = requests.post(url, headers=headers, json=data)

#         # Log the response for debugging
#         print(f"Response for {mobile}: {response.status_code}, {response.text}")
        
#         # Try parsing the response to see if it's JSON
#         try:
#             response_data = response.json()
#             # Log parsed response data
#             print(f"Parsed Response for {mobile}: {response_data}")
            
#             # Check if the message was sent successfully based on actual response data
#             if response.status_code == 200 and response_data.get('status') == "success":
#                 success_count += 1
#             else:
#                 failure_count += 1
#         except Exception as e:
#             print(f"Error parsing response for {mobile}: {str(e)}")
#             failure_count += 1

#     return {
#         "status": True if success_count > 0 else False,
#         "msg": f"Media sent: {success_count}, Failed: {failure_count}"
#     }




######################### Below code is sending dynamic PDF message when it is in live(it works for TNC) ##################################

import frappe
import requests

@frappe.whitelist()
def bulk_send_whatsapp_media_document_pdf(template_name):
    print("Template Name:", template_name)
    # Fetch the WhatsApp configuration with default set to 1
    config = frappe.get_all(
        "WhatsApp Message Configuration",
        filters={'default': 1},
        fields=['name', 'user_id', 'waba_number', 'wa_server', 'output', 'api_key', 'password']
    )
    print("Config Fetched:", config)
    # Check if configuration is available
    if not config:
        return {"status": False, "msg": "WhatsApp configuration not found."}
    
    
    # Extract the first (and assumed only) configuration since get_all returns a list
    config_doc = config[0]
    admin_settings = frappe.get_doc('WhatsApp Message Configuration', config_doc['name'])
    converted_api_key = admin_settings.get_password('api_key')
    print(converted_api_key)
    if admin_settings.active == 0:
        return {"status": False, "msg": "WhatsApp configuration is inactive."}
    
    # Fetch all documents with the "mobile", "last_name", and "amount" fields from the "Bulk WhatsApp" doctype
    bulk_whatsapp_docs = frappe.get_all("Bulk WhatsApp", filters={}, fields=["mobile", "last_name", "amount","name"])
    print("Numbers fetched:", bulk_whatsapp_docs)

    if not bulk_whatsapp_docs:
        return {"status": False, "msg": "No mobile numbers found."}

    # Prepare the list of mobile numbers from the fetched docs
    mobile_numbers = [doc['mobile'] for doc in bulk_whatsapp_docs if doc['mobile']]
    print("Mobile numbers:", mobile_numbers)
    
    if not mobile_numbers:
        return {"status": False, "msg": "No valid mobile numbers found."}

    # Fetch the template details
    template_doc = frappe.get_doc("WhatsApp Templates", template_name)
    
    if not template_doc:
        return {"status": False, "msg": "Template not found."}

    # Define the API endpoint and headers
    url = f"{config_doc['wa_server']}/send"
    headers = {
        "apikey": converted_api_key,  # Fetching API key dynamically
        "Content-Type": "application/json"
    }

    # Define the common data for sending media
    common_data = {
        "userid": config_doc['user_id'],  # Fetch user ID dynamically
        "wabaNumber": config_doc['waba_number'],  # Fetch WABA number dynamically
        "output": config_doc['output'],  # Fetch output format dynamically
        "sendMethod": template_doc.send_method,  # Use the template's send method
        "msgType": template_doc.message_type,  # Use the template's message type
        "templateName": template_doc.template_name,  # Name of the document being sent
        # "mediaUrl": template_doc.media_url,  # Use the template's media URL
        "mediaType": template_doc.media_type,  # Use the template's media type
        # "msg" : template_doc.body, # Use the template's
    }

    # Track media sending status
    success_count = 0
    failure_count = 0

    # Loop through each mobile number and send the media file with a customized message
    for doc in bulk_whatsapp_docs:
        mobile = doc['mobile']
        # last_name = doc['last_name']
        # amount = doc['amount']
        # id_of_candidate = doc['name']

        # Prepare the dynamic message
        # message = f"Dear Customer,\nYour name is {last_name}\nYour Invoice amount is {amount}"
        
        ### Below URL is the dynamica URL for PDF's ########
        # mediaUrl = f"http://192.168.1.188:8002/api/method/frappe.utils.print_format.download_pdf?doctype=Bulk%20WhatsApp&name={id_of_candidate}&format=Standard&no_letterhead=1&letterhead=No%20Letterhead&settings=%7B%7D&_lang=en"
        mediaUrl = "https://tourism.gov.in/sites/default/files/2019-04/dummy-pdf_2.pdf"
        # Copy the common data and add the mobile number and the customized message
        data = common_data.copy()
        data["mobile"] = mobile
        data['mediaUrl'] = mediaUrl
        # data["msg"] = message  # Add the dynamic message

        # Send the POST request to WhatsApp API
        response = requests.post(url, headers=headers, json=data)

        # Log the response for debugging
        print(f"Response for {mobile}: {response.status_code}, {response.text}")
        
        # Try parsing the response to see if it's JSON
        try:
            response_data = response.json()
            # print("This is responseeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",response_data)
            # Log parsed response data
            # print(f"Parsed Response for {mobile}: {response_data}")
            
            # Check if the message was sent successfully based on actual response data
            if response.status_code == 200 and response_data.get('status') == "success":
                success_count += 1
            else:
                failure_count += 1
        except Exception as e:
            print(f"Error parsing response for {mobile}: {str(e)}")
            failure_count += 1
    if success_count > 0:
        re = "All whatsapp messages sent successfully"
        if success_count < len(bulk_whatsapp_docs):

            re = f"Media sent: {success_count}, Failed: {failure_count}"

        return {
            "status": True,
            "msg": re
        }
    else:
        return {
            "status": False,
            "msg": f"Media sent: {success_count}, Failed: {failure_count}"
        }


######################## Below code is custom Text message #################################################################

@frappe.whitelist()
def bulk_send_whatsapp_text_template(template_name):
    # Fetch the WhatsApp configuration
    config = frappe.get_all(
        "WhatsApp Message Configuration",
        filters={'default': 1},
        fields=['name', 'user_id', 'waba_number', 'wa_server', 'output', 'api_key', 'password']
    )
    
    # Check if configuration is available
    if not config:
        return {"status": False, "msg": "WhatsApp configuration not found."}
    
    # Extract the first (and assumed only) configuration since get_all returns a list
    config_doc = config[0]
    admin_settings = frappe.get_doc('WhatsApp Message Configuration', config_doc['name'])
    api_key = admin_settings.get_password('api_key')  # Get the API key securely

    if admin_settings.active == 0:
        return {"status": False, "msg": "WhatsApp configuration is inactive."}

    
    # Fetch all documents with the "mobile" field from the "Bulk WhatsApp" doctype
    bulk_whatsapp_docs = frappe.get_all("Bulk WhatsApp", filters={}, fields=["mobile"])
    
    if not bulk_whatsapp_docs:
        return {"status": False, "msg": "No mobile numbers found."}

    # Prepare the list of mobile numbers
    mobile_numbers = [doc.mobile for doc in bulk_whatsapp_docs if doc.mobile]
    
    if not mobile_numbers:
        return {"status": False, "msg": "No valid mobile numbers found."}
    
    # Fetch template details dynamically (for example, assuming 'Template Doctype' holds the details)
    # Fetch the template details
    template_doc = frappe.get_doc("WhatsApp Templates", template_name)
    
    if not template_doc:
        return {"status": False, "msg": "Template not found."}
    
    # Prepare common data using the configuration and template details
    common_data = {
        "userid": config_doc['user_id'],  # Fetch user ID dynamically
        "wabaNumber": config_doc['waba_number'],  # Fetch WABA number dynamically
        "output": config_doc['output'],  # Fetch output format dynamically
        "sendMethod": template_doc.send_method,  # Use the template's send method
        "msgType": template_doc.message_type,  # Use the template's message type
        "templateName": template_doc.template_name,  # Fetch template name dynamically
    }
    
    # Define the API endpoint and headers
    url = f"{config_doc['wa_server']}/send" # Use the WA server dynamically from configuration
    headers = {
        "apikey": api_key,  # Securely fetched API key
        "Content-Type": "application/json"
    }
    
    # Track message sending status
    success_count = 0
    failure_count = 0
    
    # Loop through each mobile number and send the message
    for mobile in mobile_numbers:
        data = common_data.copy()  # Use common data and update mobile
        
        data["mobile"] = mobile
        
        # Send the POST request to WhatsApp API
        response = requests.post(url, headers=headers, json=data)

        # Log the response for debugging
        print(f"Response for {mobile}: {response.status_code}, {response.text}")
        
        # Try parsing the response to see if it's JSON
        try:
            response_data = response.json()
            # Log parsed response data
            print(f"Parsed Response for {mobile}: {response_data}")
            
            # Check if the message was sent successfully based on actual response data
            if response.status_code == 200 and response_data.get('status') == "success":
                success_count += 1
            else:
                failure_count += 1
        except Exception as e:
            print(f"Error parsing response for {mobile}: {str(e)}")
            failure_count += 1

    if success_count > 0:
        re = "All whatsapp messages sent successfully"
        if success_count < len(bulk_whatsapp_docs):

            re = f"Media sent: {success_count}, Failed: {failure_count}"

        return {
            "status": True,
            "msg": re
        }
    else:
        return {
            "status": False,
            "msg": f"Media sent: {success_count}, Failed: {failure_count}"
        }


############################### Below code is for sending Images Templates #########################################################

import frappe
import requests

@frappe.whitelist()
def bulk_send_whatsapp_media_image(template_name):
    # Fetch the WhatsApp configuration dynamically
    config = frappe.get_all(
        "WhatsApp Message Configuration",
        filters={'default': 1},
        fields=['name', 'user_id', 'waba_number', 'wa_server', 'output', 'api_key', 'password']
    )
    
    # Check if configuration is available
    if not config:
        return {"status": False, "msg": "WhatsApp configuration not found."}
    
    # Extract the first (and assumed only) configuration
    config_doc = config[0]
    admin_settings = frappe.get_doc('WhatsApp Message Configuration', config_doc['name'])
    api_key = admin_settings.get_password('api_key')  # Get the API key securely

    if admin_settings.active == 0:
        return {"status": False, "msg": "WhatsApp configuration is inactive."}
    
    # Fetch all documents with the "mobile" field from the "Bulk WhatsApp" doctype
    bulk_whatsapp_docs = frappe.get_all("Bulk WhatsApp", filters={}, fields=["mobile"])
    print("Numbers fetched:", bulk_whatsapp_docs)

    if not bulk_whatsapp_docs:
        return {"status": False, "msg": "No mobile numbers found."}

    # Prepare the list of mobile numbers
    mobile_numbers = [doc.mobile for doc in bulk_whatsapp_docs if doc.mobile]
    print("Mobile numbers:", mobile_numbers)
    
    if not mobile_numbers:
        return {"status": False, "msg": "No valid mobile numbers found."}

    # Fetch the template details dynamically
    template_doc = frappe.get_doc("WhatsApp Templates", template_name)
    
    if not template_doc:
        return {"status": False, "msg": "Template not found."}
    
    # Define the API endpoint and headers dynamically using config
    url = f"{config_doc['wa_server']}/send"
    headers = {
        "apikey": api_key,  # Securely fetched API key
        "Content-Type": "application/json"
    }

    # Define the common data dynamically using the configuration and template details
    common_data = {
        "userid": config_doc['user_id'],  # User ID from the config
        "wabaNumber": config_doc['waba_number'],  # WABA number from the config
        "output": config_doc['output'],  # Output format
        "sendMethod": template_doc.send_method,  # Use the template's send method
        "msgType": template_doc.message_type,  # Hardcoded as 'media' since we are sending media
        "templateName": template_doc.template_name,  # Template name from the template
        "mediaType": template_doc.media_type,  # Dynamic media type (e.g., image, video)
        "mediaId": template_doc.media_id  # Dynamic media ID for the media content
        # "mediaUrl": template_doc.media_url  # Dynamic media URL for the media content
    }

    # Track media sending status
    success_count = 0
    failure_count = 0

    # Loop through each mobile number and send the media
    for mobile in mobile_numbers:
        data = common_data.copy()  # Copy the common data
        data["mobile"] = mobile  # Update mobile number
        
        # Send the POST request to WhatsApp API
        response = requests.post(url, headers=headers, json=data)

        # Log the response for debugging
        print(f"Response for {mobile}: {response.status_code}, {response.text}")
        
        # Try parsing the response to see if it's JSON
        try:
            response_data = response.json()
            print(f"Parsed Response for {mobile}: {response_data}")
            
            # Check if the message was sent successfully based on actual response data
            if response.status_code == 200 and response_data.get('status') == "success":
                success_count += 1
            else:
                failure_count += 1
        except Exception as e:
            print(f"Error parsing response for {mobile}: {str(e)}")
            failure_count += 1

    # Return the success and failure counts
    if success_count > 0:
        re = "All whatsapp messages sent successfully"
        if success_count < len(bulk_whatsapp_docs):
            re = f"Media sent: {success_count}, Failed: {failure_count}"

        return {
            "status": True,
            "msg": re
        }
    else:
        return {
            "status": False,
            "msg": f"Media sent: {success_count}, Failed: {failure_count}"
        }



####################### Validating the whatsApp #################

@frappe.whitelist()
def validate_official_whatsapp_instance(config_id="WA-Config-05"):
    # Fetch the WhatsApp configuration by ID or default to WA-Config-05
    config = frappe.get_doc('WhatsApp Message Configuration', config_id)

    # Check if the configuration exists
    if not config:
        return {"status": False, "msg": "WhatsApp configuration not found."}

    # Check if both 'active' and 'default' are checked
    if not config.active or not config.default:
        if not config.active:
            return {"status": False, "msg": "WhatsApp instance is not active."}
        elif not config.default:
            return {"status": False, "msg": "WhatsApp instance is not set as default."}
    
    # If both are checked, return success
    return {"status": True, "msg": "WhatsApp instance is valid."}

@frappe.whitelist()
def send_whatsapp_text_message(mobile_number, template_name, config_id):
    # Validate the WhatsApp instance
    validation_response = validate_official_whatsapp_instance(config_id)
    
    if not validation_response.get("status"):
        return validation_response  # Return the validation failure message
    
    try:
        # Fetch the WhatsApp configuration using config_id
        config = frappe.get_doc("WhatsApp Message Configuration", config_id)
    except frappe.DoesNotExistError:
        return {"status": False, "msg": "WhatsApp configuration not found."}
    
    try:
        # Fetch the template details using frappe.get_all to filter by template_name field
        template_data = frappe.get_all(
            "WhatsApp Templates", 
            filters={"template_name": template_name},
            fields=["name"]
        )
        
        if not template_data:
            return {"status": False, "msg": "Template not found."}
        
        # Since get_all returns a list, fetch the first matching template name
        template_doc = frappe.get_doc("WhatsApp Templates", template_data[0].name)
        
    except frappe.DoesNotExistError:
        return {"status": False, "msg": "Template not found."}

    # Securely fetch API key
    api_key = config.get_password('api_key')

    # Prepare the common message data
    common_data = {
        "userid": config.user_id,  # Use user ID from config
        "wabaNumber": config.waba_number,  # WhatsApp Business Account Number
        "output": config.output,  # Output format
        "sendMethod": template_doc.send_method,  # Method from template
        "msgType": template_doc.message_type,  # Message type from template
        "templateName": template_doc.template_name,  # Template name
        "mobile": mobile_number
    }

    # Define the API endpoint and headers
    url = f"{config.wa_server}/send"  # WhatsApp API server URL from configuration
    headers = {
        "apikey": api_key,
        "Content-Type": "application/json"
    }

    # Send the POST request to WhatsApp API
    try:
        response = requests.post(url, headers=headers, json=common_data)
        print(f"Response for {mobile_number}: {response.status_code}, {response.text}")

        # Parse response
        response_data = response.json()

        # Check for success or failure
        if response.status_code == 200 and response_data.get('status') == "success":
            return {"status": True, "msg": "WhatsApp message sent successfully."}
        else:
            return {"status": False, "msg": f"Failed to send message: {response_data.get('error', 'Unknown error')}."}
    
    except requests.exceptions.RequestException as e:
        return {"status": False, "msg": f"Error while sending message: {str(e)}"}



######################### After changing to generic API(sending the Media (Document) message) ################################
import frappe
import requests

@frappe.whitelist()
def send_whatsapp_media_document_message(config_id, mobile_number, template_name, mediaUrl=None):
    validation_response = validate_official_whatsapp_instance(config_id)
    
    if not validation_response.get("status"):
        return validation_response  # Return the validation failure message
    
    try:
        # Fetch the WhatsApp configuration using config_id
        config_doc = frappe.get_doc("WhatsApp Message Configuration", config_id)
    except frappe.DoesNotExistError:
        return {"status": False, "msg": "WhatsApp configuration not found."}

    # Fetch the template details using frappe.get_all to filter by template_name field
    template_data = frappe.get_all(
        "WhatsApp Templates", 
        filters={"template_name": template_name},
        fields=["name"]
    )
    
    if not template_data:
        return {"status": False, "msg": "Template not found."}
    
    # Fetch the template document using the name from get_all result
    template_doc = frappe.get_doc("WhatsApp Templates", template_data[0].name)

    # Define the API endpoint and headers
    url = f"{config_doc.wa_server}/send"
    headers = {
        "apikey": config_doc.get_password('api_key'),  # Fetching API key dynamically
        "Content-Type": "application/json"
    }

    # Determine the media URL to use
    effective_media_url = mediaUrl if mediaUrl else template_doc.media_url
    print("<edoaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",effective_media_url)

    # Check if media URL is available
    if not effective_media_url:
        return {"status": False, "msg": "No media URL provided or available in the template."}

    # Prepare the common data for sending media
    common_data = {
        "userid": config_doc.user_id,
        "wabaNumber": config_doc.waba_number,
        "output": config_doc.output,
        "sendMethod": template_doc.send_method,
        "msgType": template_doc.message_type,
        "templateName": template_doc.template_name,
        "mediaType": template_doc.media_type,
        "mediaUrl": effective_media_url
    }

    # Track media sending status
    success_count = 0
    failure_count = 0

    # Prepare data for sending the media file
    data = common_data.copy()
    data["mobile"] = mobile_number

    # Send the POST request to WhatsApp API
    response = requests.post(url, headers=headers, json=data)

    # Log the response for debugging
    print(f"Response for {mobile_number}: {response.status_code}, {response.text}")

    # Try parsing the response to see if it's JSON
    try:
        response_data = response.json()
        
        # Check if the message was sent successfully based on actual response data
        if response.status_code == 200 and response_data.get('status') == "success":
            success_count += 1
        else:
            failure_count += 1
    except Exception as e:
        print(f"Error parsing response for {mobile_number}: {str(e)}")
        failure_count += 1

    # Return success or failure message
    if success_count > 0:
        msg = "All WhatsApp messages sent successfully" if failure_count == 0 else f"Media sent: {success_count}, Failed: {failure_count}"
        return {
            "status": True,
            "msg": msg
        }
    else:
        return {
            "status": False,
            "msg": f"Media sent: {success_count}, Failed: {failure_count}"
        }


######################### After changing to generic API(sending the Media Image message) ################################ 
import frappe
import requests

@frappe.whitelist()
def send_whatsapp_media_image(config_id, mobile_number, template_name, mediaUrl=None):
    # Fetch the WhatsApp configuration based on the provided config_id
    validation_response = validate_official_whatsapp_instance(config_id)
    
    if not validation_response.get("status"):
        return validation_response  # Return the validation failure message
    
    try:
        # Fetch the WhatsApp configuration using config_id
        config_doc = frappe.get_doc("WhatsApp Message Configuration", config_id)
    except frappe.DoesNotExistError:
        return {"status": False, "msg": "WhatsApp configuration not found."}
    
    # Fetch the template details using frappe.get_all to filter by template_name
    template_data = frappe.get_all(
        "WhatsApp Templates", 
        filters={"template_name": template_name},
        fields=["name"]
    )
    
    if not template_data:
        return {"status": False, "msg": "Template not found."}

    # Fetch the template document using the name from get_all result
    template_doc = frappe.get_doc("WhatsApp Templates", template_data[0].name)

    # Determine the media to use
    media_id = None
    media_url = None

    # Check if mediaUrl is provided
    if mediaUrl:
        media_url = mediaUrl
    # Otherwise, check for mediaId or mediaUrl in the template
    elif template_doc.media_id:
        media_id = template_doc.media_id
    elif template_doc.media_url:
        media_url = template_doc.media_url
    else:
        return {"status": False, "msg": "Neither mediaUrl nor mediaId is provided."}

    # Define the API endpoint and headers dynamically using config_doc
    url = f"{config_doc.wa_server}/send"
    headers = {
        "apikey": config_doc.get_password('api_key'),  # Get the API key securely
        "Content-Type": "application/json"
    }

    # Define the data for sending the media
    data = {
        "userid": config_doc.user_id,  # User ID from the config
        "wabaNumber": config_doc.waba_number,  # WABA number from the config
        "output": config_doc.output,  # Output format
        "sendMethod": template_doc.send_method,  # Use the template's send method
        "msgType": template_doc.message_type,  # Dynamic media type (e.g., image, video)
        "templateName": template_doc.template_name,  # Template name from the template
        "mediaType": template_doc.media_type,  # Media type (e.g., image, video)
        "mobile": mobile_number  # Provided mobile number
    }

    # Pass either mediaId or mediaUrl, whichever is available
    if media_id:
        data["mediaId"] = media_id
    elif media_url:
        data["mediaUrl"] = media_url

    # Send the POST request to WhatsApp API
    response = requests.post(url, headers=headers, json=data)

    # Log the response for debugging
    print(f"Response for {mobile_number}: {response.status_code}, {response.text}")
    
    # Try parsing the response to see if it's JSON
    try:
        response_data = response.json()
        print(f"Parsed Response for {mobile_number}: {response_data}")
        
        # Check if the message was sent successfully based on the response data
        if response.status_code == 200 and response_data.get('status') == "success":
            return {
                "status": True,
                "msg": "WhatsApp message sent successfully."
            }
        else:
            return {
                "status": False,
                "msg": f"Failed to send WhatsApp message: {response_data.get('error')}"
            }
    except Exception as e:
        print(f"Error parsing response for {mobile_number}: {str(e)}")
        return {
            "status": False,
            "msg": "Failed to send WhatsApp message due to parsing error."
        }
