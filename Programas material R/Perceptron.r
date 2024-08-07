#Investigar:https://cran.r-project.org/web/packages/magick/vignettes/intro.html
library(ggplot2)

problema <- data.frame(X1 = c(0,1,0,1), X2 = c(0,0,1,1), T=rep(1,4), E_Clase = factor(x=c("N","N","N","P")))

g <- qplot(x=X1, y=X2, data=problema, main="Funcion AND", xlab = "X1", ylab = "X2", shape=E_Clase, color=E_Clase) + geom_point(cex=5)

maxT <- 1000
t <- 0
w <- runif(3,-0.5,0.5)
wp <- w + 0.0001
 
tmpX <- (-w[3]/w[2] + w[2]/(2*w[1]) - 0.5) / (w[2]/w[1] + w[1]/w[2])
if(tmpX > 1)
  tmpX <- 1
if(tmpX < 0)
  tmpX <- 0
tmpY <- -w[1]/w[2]*tmpX - w[3]/w[2]
if(tmpY > 1)
  tmpY <- 1
if(tmpY < 0)
  tmpY <- 0
g + geom_abline(slope= (-w[1]/w[2]), intercept=(-w[3]/w[2]), color="lightblue", lty=2, lwd=1.5) + 
  annotate("text",x= 0.5, y = 0.5, label=paste("(",round(w[1],2),")x1+(",round(w[2],2),")x2+(",round(w[3],2),")=0",sep="")) + 
  annotate("segment", x = 0.5, xend = tmpX, y = 0.5 , yend = tmpY , colour = "darkgray", size = 1, arrow = arrow())
ggsave(filename = paste("perceptron",t,".jpg", sep=""), width = 10, height = 7)
while (t < maxT & !all(wp == w)) {
  orden <- sample(1:4)
  wp <- w
  for (o in orden) {
    p <- sum(problema[o,1:3] * w)
    if((problema[o,4] == "P" & p > 0) | (problema[o,4] == "N" & p < 0)){
      next
    }
    else if (problema[o,4] == "P" & p <= 0){
      w <- as.vector(w + problema[o,1:3])
      t <- t + 1
    }
    else if (problema[o,4] == "N" & p >= 0){
      w <- as.vector(w - problema[o,1:3])
      t <- t + 1
    }
    if(!all(w == wp)){
      tmpX <- (-w$T/w$X2 + w$X2/(2*w$X1) - 0.5) / (w$X2/w$X1 + w$X1/w$X2)
      if(tmpX > 1)
        tmpX <- 1
      if(tmpX < 0)
        tmpX <- 0
      tmpY <- -w$X1/w$X2*tmpX - w$T/w$X2
      if(tmpY > 1)
        tmpY <- 1
      if(tmpY < 0)
        tmpY <- 0
      g + geom_abline(intercept = (-w$T/w$X2), slope = (-w$X1/w$X2), color="lightblue", lty=2, lwd=1.5) + 
        annotate("text",x= 0.5, y = 0.5, label=paste("(",round(w[1],2),")x1+(",round(w[2],2),")x2+(",round(w[3],2),")=0",sep="")) +
        annotate("segment", x = 0.5, xend = tmpX, y = 0.5 , yend = tmpY , colour = "darkgray", size = 1, arrow = arrow())
      ggsave(filename = paste("perceptron",t,".jpg", sep=""), width = 10, height = 7)
    }
  }
}

prediccion <- c()
for (r in 1:4){
  t <- sum(problema[r,1:3] * w)
  if(t >= 0)
    prediccion <- c(prediccion, "P")
  else
    prediccion <- c(prediccion, "N")
}
problema$Prediccion <- prediccion
print(problema)
