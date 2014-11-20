install.packages("devtools")
install.packages("rjson")
library("devtools")
library("rjson")
json_file <- "tweets.json"
json_data <- fromJSON(file=json_file)

