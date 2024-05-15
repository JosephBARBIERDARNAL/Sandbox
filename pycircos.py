

values_all   = [] 
arcdata_dict = collections.defaultdict(dict)
with open("pycircos/sample_data/example_data_rect_gradual.csv") as f:
   f.readline()
   for line in f:
      line  = line.rstrip().split(",")
      name  = line[0]     
      start = int(line[1])-1
      end   = int(line[2]) 
      width = end-start 
      if name not in arcdata_dict:
            arcdata_dict[name]["positions"] = []
            arcdata_dict[name]["widths"]    = [] 
            arcdata_dict[name]["values"]    = [] 
      arcdata_dict[name]["positions"].append(start) 
      arcdata_dict[name]["widths"].append(width)
      arcdata_dict[name]["values"].append(float(line[-1]))
      values_all.append(float(line[-1]))

vmin, vmax = min(values_all), max(values_all) 
for key in arcdata_dict:
   circle.heatmap(key, data=arcdata_dict[key]["values"], positions=arcdata_dict[key]["positions"], 
                  width=arcdata_dict[key]["widths"], raxis_range=[630,670], vmin=vmin, vmax=vmax, 
                  cmap=plt.cm.viridis)


# wrap in a function
def circle_heatmap(
      data_file, 
      raxis_range=[630,670], 
      vmin=None, 
      vmax=None, 
      cmap=plt.cm.viridis
      ):
      values_all   = [] 
      arcdata_dict = collections.defaultdict(dict)
      with open(data_file) as f:
         f.readline()
         for line in f:
               line  = line.rstrip().split(",")
               name  = line[0]     
               start = int(line[1])-1
               end   = int(line[2]) 
               width = end-start 
               if name not in arcdata_dict:
                  arcdata_dict[name]["positions"] = []
                  arcdata_dict[name]["widths"]    = [] 
                  arcdata_dict[name]["values"]    = [] 
               arcdata_dict[name]["positions"].append(start) 
               arcdata_dict[name]["widths"].append(width)
               arcdata_dict[name]["values"].append(float(line[-1]))
               values_all.append(float(line[-1]))
   
      vmin, vmax = min(values_all), max(values_all) 
      for key in arcdata_dict:
         circle.heatmap(key, data=arcdata_dict[key]["values"], positions=arcdata_dict[key]["positions"], 
                        width=arcdata_dict[key]["widths"], raxis_range=raxis_range, vmin=vmin, vmax=vmax, 
                        cmap=cmap)
)

circle_heatmap("pycircos/sample_data/example_data_rect_gradual.csv")
