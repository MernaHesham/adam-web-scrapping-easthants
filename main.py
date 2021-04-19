from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.easthants.ca/government/council/meeting-minutes-and-agendas/')
contents = page.content
soup = BeautifulSoup(contents, features = 'lxml')

divTag = soup.find_all("table", {"class": "table table-hover"})
# print(divTag)


Col_name = []
for tag in divTag:
    tdTags = tag.find_all("th")
    for tag in tdTags:
        print(tag.text)
        Col_name.append(tag.text)
print('\n')
print(Col_name)
print('---------------------------------')
print('\n')


col1 = []
for tag in divTag:
    tdTags = tag.find_all("span", {"class": "visible-xs-inline"})
    for tag in tdTags:
        print(tag.text)
        col1.append(tag.text.strip())
print('\n')
print(col1)
print('---------------------------------')
print('\n')




col2 = []
for tag in divTag:
    tdTags = tag.find_all("td")
    for tag in tdTags:
        # print(tag.text.strip())
        col2.append(tag.text.strip())
print('\n')
print(col2)
print('---------------------------------')
print('\n')


# selecting Agenda Data
Agenda_links = []
for tag in divTag:
    tdTags = tag.find_all("a")
    for tag in tdTags:
        if tag.text.strip() == 'Agenda':
            print(tag.get('href'))
            Agenda_links.append(tag.get('href'))
print('\n')
print(Agenda_links)
print('---------------------------------')
print('\n')

agenda_file_names = []
for link in Agenda_links:
    agenda_page = requests.get(link)
    agenda_soup = BeautifulSoup(agenda_page.content, features = 'lxml')
    agenda_file_name = agenda_soup.find('div', {"class":"col-xs-12 col-sm-9 template-content"}).h1.text
    agenda_file_names.append(agenda_file_name)
    print(agenda_file_name)
    agenda_components = agenda_soup.find_all('div', {"class":"row occ-agenda-component"})
    for agenda_component in agenda_components:
        print(agenda_component)
    agenda_file_text = agenda_soup.find('div', {"class":"row occ-agenda-component"}).text.strip()
    agenda_file = open(agenda_file_name + ".txt", "w")
    agenda_file.write(agenda_file_text)
    agenda_file.close()

print('\n')
print(agenda_file_names)
print('---------------------------------')
print('\n')


# agenda_content = []
# for link in Agenda_links:
#     agenda_page = requests.get(link)
#     agenda_soup = BeautifulSoup(agenda_page.content, features = 'lxml')
#     # agenda_content.append(agenda_soup.find('div', {"class":"col-xs-12 col-sm-9 template-content"}).text)
#     print(agenda_soup.find('div', {"class":"template-body"}).text.strip())
#     print("End of texttttttttttttttttttttttttttttttttttttttttttttttttttttt")

# print('\n')
# print(agenda_content)
# print('---------------------------------')
# print('\n')

# print(soup.find_all('a'))