install.packages("ROAuth")
install.packages("RCurl")
library(ROAuth)
library(ROAuth)
library(twitteR)
library(RCurl)
library(streamR)
#library(topic models)
### Authentications part
options(RCurlOptions = list(cainfo = system.file("CurlSSL", "cacert.pem", package = "RCurl")))
reqURL <- "https://api.twitter.com/oauth/request_token"
accessURL <- "https://api.twitter.com/oauth/access_token"
authURL <- "https://api.twitter.com/oauth/authorize"
consumerKey <- "Tsttw9p06eUjr2xoKWv9NTkYq"
consumerSecret <- "87ofvyPQJYcAox1QA8ufwTlWF8fvsHXgwitpHHOGFh6ite4jFd"
twitCred <- OAuthFactory$new(consumerKey=consumerKey,
                             consumerSecret=consumerSecret,
                             requestURL=reqURL,
                             accessURL=accessURL,
                             authURL=authURL)
twitCred$handshake()
save(twitCred, file="~/Projects/SocialMediaAndArabSpring/.twitteR_creds")
load("~/Projects/SocialMediaAndArabSpring/.twitteR_creds")
registerTwitterOAuth(twitCred)
######## Extract data from twitter using streamR
filterStream(“tweets.json”, track = c(“Libya”, “Egypt”), tweets=150, timeout = 36000, oauth = twitCred)
