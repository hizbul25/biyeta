## Biyeta.com Crawler
http://biyeta.com is a match making website in Bangladesh. See all of the matching person information is quite
painful. If n number of peoples profile get match with my preference then i need to visit n profile to check who is the best.
This crawler export n profile information into a csv file within a minute. Then you can check who is the best within a sing sheet.

## Usage
I guess you have a account in http://biyeta.com and you have completed your profile.
1. Install scrapy in your machine `pip install scrapy`
2. Go to project directory `$ cd biyeta`
3. Set login credential to `settings.py` file.
    `USER_NAME = 'someemail@gmail.com'`
     `PASSWORD = 'pass'`
4. Run command `scrapy crawl biye`

You will get a CSV file in your project directory containing matching data.

## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D