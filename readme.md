[Hirefy](https://hirefyapp.herokuapp.com/), a no login platform for hiring managers to find suitable candidates for any positions

## Features
1. No login required for the hiring managers to view and save the potential applicants.
2. All the applicants in this platform are verifed and constantly being verifed by the hirefy team.
3. Reduced clicks, so less hassle compared to other platforms.
4. Simple UI, so your not distracted.
4. If you are an applicant, you have to signup with a simple signup form and just need to provide the necessary details to showcase your skills to the hiring managers.

## Project details
This project is using [flask](https://flask.palletsprojects.com/en/2.2.x/) as their backend framework and uses [Harperdb](https://harperdb.io/) as their database.

## Harperdb
1. This project uses [Harperdb](https://harperdb.io/) for its 95% data related needs
2. This project uses thier python [SDK](https://pypi.org/project/harperdb/) to interact with thier application

## Project Walkthrough
Currently, hirefy has 5 pages namely homepage, saved applicants page, applicant login page, applicant register page, and applicant profile detail page

![hirefy_homepage](https://user-images.githubusercontent.com/72196714/187074913-59d97f24-3653-43f2-9949-c33f65ad9c6d.jpg)

1. This is where hiring manager can find all his saved applicants.
2. This is where an applicant can login to his account.
3. This is where you can search for applicants.
4. filters to filter the applicants based on the hiring manager's needs.
5. Category box, this is where hiring manager can see different categories and count of applicants in each category.

![hirefy_slide](https://user-images.githubusercontent.com/72196714/187075180-d278b8c0-cf18-4a2d-af51-61ae5543fc28.jpg)

#### Once hiring manager clicks any of the category they will be taken to this slide element

6. This is where hiring manager can save a applicant for later inspection.
7. This is where a hiring manager can view the full detailed profile of the selected candidate.
8. To move to the next candidate, you could use mouse or keyboard arrow keys to do this.
9. Each and every applications goes through hirefy team for verification, once verified they will recieve this verified badge.

![hirefy_slide_not_verified](https://user-images.githubusercontent.com/72196714/187075388-e5c743c3-6122-4ac3-ba8f-b1542d9cf726.jpg)

10. If verification is on process, they will recieve this on process badge.

![hirefy_unsave](https://user-images.githubusercontent.com/72196714/187075416-23828b82-2606-4cea-a937-11ac25314ada.jpg)

11. Once you click save profile the button will change to unsave profile, if you click it again it will unsave the profile.

![hirefy_saved_applicant](https://user-images.githubusercontent.com/72196714/187075460-aad68e73-3ef4-4a83-9769-c9808698a161.jpg)

12. If you have clicked saved applicants link (1), then this is how it will look like where you can see all the saved applicants in a list view.

![hirefy_profile_detail](https://user-images.githubusercontent.com/72196714/187075534-68f15c5a-0d9c-41c4-948a-95e46c4d0588.jpg)

This is how the profile detail page will look, this is where hiring manager can look for detailed profile on the applicant if interested.

![hirefy_login_applicant](https://user-images.githubusercontent.com/72196714/187075855-ea92b6dd-d583-4c71-89da-004966007df6.jpg)

13. If you are an applicant you have to register an account with us, after that this is where you have to login
14. This roject currently is in prototype stage, so for the ease of navigating we have provided an dummy username and password (login process is only required if your an applicant, if your an hiring manager you don't have to login and can still use all of our hiring features).

![hirefy_logged_in_navbar](https://user-images.githubusercontent.com/72196714/187076028-2e0aae45-3de5-4880-a52a-59f555414a9f.jpg)

15. Once an applicant is logged in he will redirected to the homepage where the navbar has changed, now it has logout and profile settings/update/view url.

![hirefy_applicant_profile_settings](https://user-images.githubusercontent.com/72196714/187076790-1f97b305-199a-4c11-b439-d81b9b71903e.jpg)

This is how the profile settings/update/view will look like.

## Future
If i am continuing with this project, i would like to make this platform more skill based rather than degree based that means any applicant with right skill sets can come and showcase thier skills in this platform, we in hirefy would amplify it to the hiring managers. This can be done through various techniques and one of them which comes to my mind is having a skill assessment test for each category where after qualifying they will be having a skill badge near to thier profile (something like linkedin skill assessment test, but better) 

I would also like to add advanced filters and bring improvements to UI/UX.

## Acknowlegments

Thanks Dennis Ivy and partners [Harperdb](https://harperdb.io/) and [Agora](https://www.agora.io/en/) for sponsoring this hackathon. This hackathon will help the participants gain new experiences and not only that the winners will have some sort an encouragement to go on and pursue thier passion.


