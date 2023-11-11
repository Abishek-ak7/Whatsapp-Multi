import re
import pywhatkit as kit
from datetime import datetime

# Sample input text

input_text = []

# Define a regular expression pattern to match phone numbers

# Define a regex pattern to match phone numbers (example: xxx-xxx-xxxx)
phone_number_pattern = r'\d{3}\d{3}\d{4}'

# Open the text file for reading
file_path = 'number.txt'
try:
    with open(file_path, 'r') as file:
        text = file.read()

    # Use the regex pattern to find all matching phone numbers in the text
    phone_numbers = re.findall(phone_number_pattern, text)

    if phone_numbers:
        print("Phone numbers found in the file:")
        for number in phone_numbers:
            input_text.append(number)
    else:
        print("No phone numbers found in the file.")

except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Sample message content
message_content = (
    "Greetings, we are from team 'ReVil' from the\n Department of CyberSecurity,\nChennai institute of technology.\n"
    "We are delighted to introduce 'REVIL,' our prestigious \nNational-Level Cybersecurity Symposium, set to take place on \nSaturday, September 23rd. \nThis event promises a dynamic day filled with \ntechnical and non-technical sessions, hands-on \nworkshops, and captivating online events. We extend a warm invitation for you to\n grace us with your presence and expertise, as your participation would \nsignificantly enrich the 'REVIL' experience for our eager attendees. Join us in\n shaping the future of cybersecurity at this exceptional gathering.\n\n"
    "\n"
    "For further updates,\n"
    "You can visit our official website,\n"
    "https://www.revil.in/\n"
    "\n"
    " You can visit our official Instagram page,\n"
    "\n"
    "https://instagram.com/revil_cit?igshid=MzRlODBiNWFlZA==\n\n"
    "\n\n"
    "For any queries,\n"
    "ABCD - 735432XXXX\n"
    "klmn J - 63803XXXXX\n"
    "GHI - 79XXXXX562\n"
    "\n"
    "\n"
    "Thank you ")

# Send the message to each phone number using pywhatkit
for phone_number in phone_numbers:
    # Format the phone number as required by pywhatkit (remove any dashes or spaces)

    # Get the current time
    current_time = datetime.now()
    image_path = "Revil.png"
    # Send the message instantly (specify current time as time_hour and time_minute)
    kit.sendwhatmsg(f"+91{phone_number}", message_content, current_time.hour, current_time.minute + 1)
    kit.sendwhats_image(f"+91{phone_number}",image_path)

    print(f"Message sent to {phone_number} instantly.")
