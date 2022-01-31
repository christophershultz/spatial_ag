library(raster)
library(comprehenr)
library(stringr)

setwd('C:/Users/cshul/Desktop/spatial_ag')

# Import data frame and shapefile
p <- shapefile(paste(getwd(), "/county_shape_file/cb_2018_us_county_5m.shp", sep = ""))
d <- read.csv(paste(getwd(), "/usda_data/joined_usda_df.csv", sep = ""))

# update d fips
newFips = list()
for (item in d$fips){
  item = str_replace(item, "-", "")
  newFips = append(newFips, item)
}
d$fips = newFips



# merge
p$fips = paste(p$STATEFP, p$COUNTYFP, sep = "")
m <- merge(p, d, by = 'fips')

# save as shapefile again
outPath = paste(getwd(), "/join_usda_to_shape/usda_shapefile.shp", sep = "")
shapefile(m, outPath, overwrite=TRUE)
