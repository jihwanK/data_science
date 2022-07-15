home = '~/git_repository/practical-statistics-for-data-scientists/data'
setwd(home)
state <- read.csv('state.csv')
hist(state[['Murder.Rate']])