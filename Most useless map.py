import google.generativeai as genai


genai.configure(api_key="GEMINI_API_KEY")


model = genai.GenerativeModel("gemini-1.5-flash")


start=input("Enter your start location:")


destination=input("Enter your final location:")


model.generate_content("my current location is in india and hence give me the response likewise,")


response = model.generate_content(f"give me just the name of the airport closest to {start}")
ap1=response


response2=model.generate_content(f"give me just the name of a random airport other than {ap1} in india")


ap2=response2

response3=model.generate_content(f"give me just the map link by car starting from  {ap2} to {destination}")

print(f''' first go to {response.text}
then from book a flight from {response.text} to {response2.text}
Then follow the following car path to {destination}
{response3.text}''')

input("Press any key to exit")
