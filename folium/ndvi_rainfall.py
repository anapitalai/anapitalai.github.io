## Library usage
from geobricks_raster_correlation.core.raster_correlation_core import get_correlation
from matplotlib import pyplot as plt
from matplotlib.pylab import polyfit, polyval


raster_path2 = "data/ndvi.tif"
raster_path1 = "data/rfall.tif"
# Number of bins to be applied to the scatter chart
bins = 300
corr = get_correlation(raster_path1, raster_path2, bins)
print corr



# Number of sampling bins
bins = 150

corr = get_correlation(raster_path1, raster_path2, bins)
x = []
y = []
colors = []
# print corr['series']
for serie in corr['series']:
   colors.append(serie['color'])
for data in serie['data']:
   x.append(data[0])
   y.append(data[1])

# Adding regression line
(m, b) = polyfit(x, y, 1)
yp = polyval([m, b], x)
plt.plot(x, yp)

# plotting scatter
plt.scatter(x, y, c=colors)
plt.show()


corr['stats'] ##contains the statistics: slope, p_value, std_err, intercept, r_value
corr['series'] ##contains the output series that can be used directly as an Highcharts input or with Matplotlib. 