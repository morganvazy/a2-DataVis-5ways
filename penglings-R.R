#Using Statistical tools for high-throughput
#data analysis ggplot2 scatter plots quick guide
#as reference

ggplot(penglings, aes(x=flipper_length_mm, y=body_mass_g)) 
+ geom_point(aes(color=species, size=bill_length_mm), alpha=0.8) 
+scale_color_manual(values = c("Adelie" = "#FA9702", "Chinstrap"="#B802FA", "Gentoo"="#018A75"))
