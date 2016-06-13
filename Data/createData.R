########################## Quick preprocessing and convert RDA-file into a csv ########################
#
# clean up
rm(list=ls(all=TRUE))

# load data 2.7 (in rda-format)
load("data_2_7_full.Rda")

# splitting into labeled and unlabeled data
class <- df[ is.na(df$returnQuantity),]
train <- df[!is.na(df$returnQuantity),]

# convert training set into a data.table 
library(data.table)
df <- data.table(train)
rm(train)


# save actual label, which are not binary in case we need them later, change write.csv to your directory
actual_labels <- df[,returnQuantity]
write.csv(actual_labels, file = "C:/Users/dkoehn/Documents/Github/AUCNN/Data/actualLabels.csv")
rm(actual_labels)

# add quarter dummies instead of yearQuarter which is badly coded into 1,2,3,4
# function form variable_creation repo
quarterDummys <- function(dt){
  temp <- dt
  # leaving out january to avoid multicolinearity
  dummyMatrix <- matrix(rep(NA,nrow(temp)*3),nrow(temp),3)
  bg <- c(4,7,10) # begining of each quarter
  for(i in 1:3){
    dummyMatrix[,i] <- as.numeric(temp[,month(orderDate)] %in% c(bg[i],(bg[i]+1),(bg[i]+2)) )
  }#end for
  
  result <- data.table(secondQuarter_dummy = dummyMatrix[,1],thirdQuarter_dummy = dummyMatrix[,2],fourthQuarter_dummy = dummyMatrix[,3])
  
  return(result)
}#end function

# actual variable creation
dummys <- quarterDummys(df)
df[,secondQuarter := dummys[,secondQuarter_dummy]]
df[,thirdQuarter := dummys[,thirdQuarter_dummy]]
df[,fourthQuarter := dummys[,fourthQuarter_dummy]]

# perform outlier detection
source("outlierDetection.R")

## Deleting all unnecessary variables for prediction
df_new <- df[, `:=`(unique_ID=NULL, orderID=NULL, orderDate=NULL, articleID=NULL, colorCode=NULL,
                  sizeCode=NULL, productGroup=NULL, voucherID=NULL,customerID=NULL,deviceID=NULL,
                  paymentMethod=NULL,special_group=NULL,yearQuarter =NULL, returnQuantity=NULL,
                  Newcommers=NULL,returningCustomer=NULL, Sale=NULL,Loyals=NULL)]


## splitting df_new into trainings(60%) and validation set(40%) 
library(caret)
ratio <- 0.6
set.seed(123)
idx.tr <- createDataPartition(df_new$returnBin, p=ratio, list=FALSE) 
train <- df_new[idx.tr,] 
validation  <- df_new[-idx.tr,]

# write data as csv-file (take 2min)
write.csv(train, file = "C:/Users/dkoehn/Documents/Github/AUCNN/Data/training.csv")
write.csv(validation, file = "C:/Users/dkoehn/Documents/Github/AUCNN/Data/validation.csv")
