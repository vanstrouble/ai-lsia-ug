library(datasets)

norma <- function(x){
  return(sum(x^2)^0.5)
}

np = 5

ds <- iris[c(1:5,51:55,101:105),3:4]

plot(ds)

norm <- apply(ds, MARGIN = 1, FUN = norma)
ds <- ds/norm

perceptron = cbind(runif(np, min(ds[,1]),max(ds[,1])),runif(np, min(ds[,2]),max(ds[,2])))

plot(ds)

norm <- apply(perceptron, MARGIN = 1, FUN = norma)
perceptron <- perceptron/norm

plot(ds) + points(perceptron, pch=3, col="blue", lwd=2)

orden <- sample(1:nrow(ds), nrow(ds), replace=F)
grupos <- data.frame(id=rep(0,nrow(ds)), gpo = rep(0,nrow(ds)))

for(i in orden){
  pp <- perceptron %*% t(ds[i,])
  df <- data.frame(per_id=1:np, met=as.vector(pp))
  df <- df[order(df$met, decreasing = T),]
  plot(ds) + points(perceptron, pch=3, col="blue", lwd=2) + points(ds[i,], col="red", lwd=2)
  perceptron[df[1,1],] <- perceptron[df[1,1],] + as.numeric(ds[i,])
  norm <- apply(perceptron, MARGIN = 1, FUN = norma)
  perceptron <- perceptron/norm
  plot(ds) + points(perceptron, pch=3, col="blue", lwd=2) + points(ds[i,], col="red", lwd=2)
  grupos[i,1] <- i
  grupos[i,2] <- df[1,1]
  #print(paste("ID Patron", i," Patron:", paste(ds[i,], collapse = " "), "ID Perceptron:",df[1,1], "Perceptron",paste(perceptron[df[1,1],], collapse = " "), sep=" "))
}
plot(ds) + points(perceptron, pch=3, col="blue", lwd=2)
print("Agrupamiento")
print(grupos)
print("Pesos Perceptrones")
print(perceptron)
