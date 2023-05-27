# Team B

## HVA CTF PROJECT for PAD 2022-2023
DedsecCTF is a project made for the CyberSecurity PAD project 2022-2023. The project is made with the Django-framework.

## Challenges
There are four challenges playable on the CTF website. They are all playable locally only, three of the challenges are in docker seperate from the website. 

Challenges in docker: Sqlinjection, webexploit en bruteforce. 
Challenge not in docker but on the website: decode challenge.

## Requirements: docker en build tools
Docker and docker-compose

## Installation
To play the challenges and run the website you need docker. Here is a link to the official page of docker with a step by step tutorial on how to install docker: https://docs.docker.com/engine/install/.

## Running/starting the project with docker

### Follow the following steps to get the main website in docker:
1. clone this git repository. (use: VSCODE)

2. click on code then on HTTPS, and copy the address.

3. Go to VSCODE paste the address in the bar that appears after you select clone this repository and click enter. 

4. next you need to select a location to clone the repository to, navigate to Desktop. Click new folder, and give the new folder a name. Then click select as repository destination.

5. next you will get a notifaction, click on open.

6. after you opened the repository you need to open up a terminal (it can take sometime before you can do this).

7. type the following command in the terminal: cd Django 

8. type the following command in the terminal: cd pad

9. then type the following command in the terminal: docker-compose build (this can take some time)

10. then type the following command in the terminal: docker-compose up

Now if you navigate to docker desktop you should see a container this is the container where the main website is located. 

You can navigate to localhost:8000 on your preffered browser to visit the website as long as the container is running. 

To clone the challenges you need to clone the other 3 branches.

### Follow the following steps to get the challenges in docker:

Brute_force challenge
1. Type the following command in the same terminal: git checkout brute_force 
2. Now open a new terminal and type the following commands: docker-compose build
3. And type the following command: docker-compose up

Now if you navigate to docker desktop you should see a container this is the container where the brute force challenge is located.
You can navigate to localhost:4000 to visit the challenge.

Webexploit challenge
1. type the following command in the same terminal: git checkout challenge2
2. Now open a new terminal and type the following commands: cd webexploit
3. Now type the following command: docker-compose build
4. And type the following command: docker-compose up

Now if you navigate to docker desktop you should see a container this is the container where the webexploit challenge is located.
You can navigate to localhost:8002 to visit the challenge.

Sqlinjection challenge
1. type the following command in the same terminal: git checkout sqlinjection_challenge
2. Now open a new terminal and type the following commands: cd sql
3. Now type the following command: docker-compose build
4. And type the following command: docker-compose up

Now if you navigate to docker desktop you should see a container this is the container where the sqlinjection challenge is located.
You can navigate to localhost:8001 to visit the challenge.

## Authors
Mete Basoda 
Bruno Blaauboer
Jerre Hilgeman
Hicham Almakroudi


