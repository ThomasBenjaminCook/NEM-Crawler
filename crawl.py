import datetime as dt
datestring = "2023/01/01"
minusedtime = dt.datetime(int(datestring.split("/")[0]),int(datestring.split("/")[1]),int(datestring.split("/")[2]))-dt.timedelta(days=9)
time = dt.datetime(int(datestring.split("/")[0]),int(datestring.split("/")[1]),int(datestring.split("/")[2]))
print(minusedtime<time)

def activate_crawler(target_directory, date_boundary, url):

    def number_to_date(number):
        year = number[0:4]
        month = number[4:6]
        day = number[6:8]
        return(year+"/"+month+"/"+day)
    
    def compare_dates(this_date,baseline_date,buffer):
        baseline_date_object_with_buffer = dt.datetime(int(baseline_date.split("/")[0]),int(baseline_date.split("/")[1]),int(baseline_date.split("/")[2]))-dt.timedelta(days=buffer)
        this_date_object = dt.datetime(int(this_date.split("/")[0]),int(this_date.split("/")[1]),int(this_date.split("/")[2]))
        return(this_date_object>=baseline_date_object_with_buffer)

    import os
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    from deleter import delete_files_in_folder
    import datetime as dt

    # Directory to save the downloaded files
    download_directory = os.path.join(os.getcwd(), target_directory) #Puts shit in current directory
    delete_files_in_folder(target_directory) #Clears the directory.

    # Send a GET request to the URL
    response = requests.get(url) #I think this asks for the html page

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser') #Soup translates it to HTML

    # Find all the <a> tags with href attributes
    links = soup.find_all('a', href=True) #Finds all the links

    # Download each zip file
    for link in links:
        # Get the absolute URL of the zip file
        file_url = urljoin(url, link['href']) #The link will just have the end of the link. Add it to main link.

        # Check if the link points to a zip file
        if file_url.endswith('.zip'):
            numberdate_selected_zip = number_to_date(((file_url.split("/")[-1]).split("_")[-1]).split(".")[0])
            if(compare_dates(numberdate_selected_zip,date_boundary)):
                # Send a GET request to download the file
                file_response = requests.get(file_url)

                # Extract the filename from the URL
                filename = os.path.basename(file_url)

                # Save the file to the download directory
                with open(os.path.join(download_directory, filename), 'wb') as f:
                    f.write(file_response.content)