######################## Outlier Detection and Scaling #############################
#
#
######## outlier detection using z-score
z_score <- function(x, threshold=3.5){
  z <- (x-mean(x))/sd(x)
  outlier <- which(z > threshold)
  return(outlier)
}

outlier_replacement <- function(x,threshold=3.5,integer=FALSE){
  outliers <- z_score(x, threshold)
  if(integer == TRUE){
    x[outliers] <- round(mean(x) + threshold * sd(x),0)
  } else {
    x[outliers] <- mean(x) + threshold * sd(x)
  }
  return(x)
}
## testcode

## outlier detection and replacement for each continuos variabel
summary(df$quantity)
table(df$quantity)
df$quantity[df$quantity>5] <- 5  # z_score does not make sense here

# rrp
summary(df$rrp)
df$rrp <- outlier_replacement(df$rrp)  


# c2umArticleCount
summary(df$cumArticleCount)
df$cumArticleCount <- outlier_replacement(df$cumArticleCount)

# totOrder
summary(df$totOrder)
df$totOrder <- outlier_replacement(df$totOrder,integer=TRUE)

# number_of_same_items_in_order
summary(df$number_of_same_items_in_order)
df$number_of_same_items_in_order <- outlier_replacement(df$number_of_same_items_in_order, integer=TRUE)

# total_items_in_order
summary(df$total_items_in_order)
df$total_items_in_order <- outlier_replacement(df$total_items_in_order, integer=TRUE)

# cheap_item_in_product_group
summary(df$cheap_item_in_product_group) # dummy no oulier

# voucher_ratio
summary(df$voucher_ratio)
df$voucher_ratio <- outlier_replacement(df$voucher_ratio)

# relative_deviation_price_mean_byOrderID
summary(df$relative_deviation_price_mean_byOrderID)
# no outlier smaller then zero
sum(df$relative_deviation_price_mean_byOrderID[z_score(df$relative_deviation_price_mean_byOrderID)] < 0)
df$relative_deviation_price_mean_byOrderID <- outlier_replacement(df$relative_deviation_price_mean_byOrderID)

# C1
summary(df$C1)
df$C1 <- outlier_replacement(df$C1, integer=TRUE)

# C2
summary(df$C2)
df$C2 <- outlier_replacement(df$C2, integer=TRUE)

# C3
summary(df$C3)
df$C3 <- outlier_replacement(df$C3, integer=TRUE)

# C4
summary(df$C4)
df$C4 <- outlier_replacement(df$C4, integer=TRUE)

# C5
summary(df$C5)
df$C5 <- outlier_replacement(df$C5, integer=TRUE)

# revenue
summary(df$revenue)
df$revenue <- outlier_replacement(df$revenue, integer=FALSE)

# voucherAmount
summary(df$voucherAmount)
df$voucherAmount <- outlier_replacement(df$voucherAmount, integer=FALSE)

# cumsmOrder
summary(df$cumsumOrder)
df$cumsumOrder <- outlier_replacement(df$cumsumOrder, integer=TRUE)

# order_per_customer
summary(df$orders_per_customer)
df$orders_per_customer <- outlier_replacement(df$orders_per_customer, integer=TRUE)

# number_of_items_from_same_category
summary(df$number_of_items_from_same_category)
df$number_of_items_from_same_category <- outlier_replacement(df$number_of_items_from_same_category, 
                                                             integer=TRUE)
#relative_deviation_price_mean_byCustomerID
summary(df$relative_deviation_price_mean_byCustomerID)
df$relative_deviation_price_mean_byCustomerID <- outlier_replacement(df$relative_deviation_price_mean_byCustomerID)

#relative_deviation_price_mean_byProductGroup
summary(df$relative_deviation_price_mean_byProductGroup)
df$relative_deviation_price_mean_byProductGroup <- outlier_replacement(df$relative_deviation_price_mean_byProductGroup)









