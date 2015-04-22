library(ggplot2)
library(splines)
Sys.setlocale("LC_TIME", "C")
d <- scan('lesson8.txt',sep='\n',what=list('','',''))
df <- data.frame('date'=as.character(c(d[1],recursive=TRUE)),
			'ip'=as.numeric(c(d[2],recursive=TRUE)),
			'pv'=as.numeric(c(d[3],recursive=TRUE)))
head(df)
qplot(ip, pv, data = df, geom = c("point", "smooth"),
                            method = "lm")
qplot(as.Date(strptime(as.character(df$date), "%a %b %d")), pv/ip,
                        data = df, geom = c("line","point","smooth"), method="lm",main="每个IP平均pv",xlab = "日期", ylab = "pv/ip")

qplot(as.Date(strptime(as.character(df$date), "%a %b %d")), pv,
                        data = df, geom = c("line","point","smooth"), method="lm",main="pv量趋势图",xlab = "日期", ylab = "pv")  
  
