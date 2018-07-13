
# coding: utf-8

# ## Project: Visualizing the Orion Constellation
# 
# In this project you are Dr. Jillian Bellovary, a real-life astronomer for the Hayden Planetarium at the American Museum of Natural History. As an astronomer, part of your job is to study the stars. You've recently become interested in the constellation Orion, a collection of stars that appear in our night sky and form the shape of [Orion](https://en.wikipedia.org/wiki/Orion_(constellation)), a warrior God from ancient Greek mythology. 
# 
# As a researcher on the Hayden Planetarium team, you are in charge of visualizing the Orion constellation in 3D using the Matplotlib function `.scatter()`. To learn more about the `.scatter()` you can see the Matplotlib documentation [here](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html). 
# 
# You will create a rotate-able visualization of the position of the Orion's stars and get a better sense of their actual positions. To achieve this, you will be mapping real data from outer space that maps the position of the stars in the sky
# 
# The goal of the project is to understand spatial perspective. Once you visualize Orion in both 2D and 3D, you will be able to see the difference in the constellation shape humans see from earth versus the actual position of the stars that make up this constellation. 
# 
# <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Orion_constellation_with_star_labels.jpg" alt="Orion" style="width: 400px;"/>
# 
# 

# ## 1. Set-Up
# The following set-up is new and specific to the project. It is very similar to the way you have imported Matplotlib in previous lessons.
# 
# + Add `%matplotlib notebook` in the cell below. This is a new statement that you may not have seen before. It will allow you to be able to rotate your visualization in this jupyter notebook.
# 
# + We will be using a subset of Matplotlib: `matplotlib.pyplot`. Import the subset as you have been importing it in previous lessons: `from matplotlib import pyplot as plt`
# 
# 
# + In order to see our 3D visualization, we also need to add this new line after we import Matplotlib:
# `from mpl_toolkits.mplot3d import Axes3D`
# 

# In[1]:


get_ipython().run_line_magic('matplotlib', '')
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# ## 2. Get familiar with real data
# 
# Astronomers describe a star's position in the sky by using a pair of angles: declination and right ascension. Declination is similar to longitude, but it is projected on the celestian fear. Right ascension is known as the "hour angle" because it accounts for time of day and earth's rotaiton. Both angles are relative to the celestial equator. You can learn more about star position [here](https://en.wikipedia.org/wiki/Star_position).
# 
# The `x`, `y`, and `z` lists below are composed of the x, y, z coordinates for each star in the collection of stars that make up the Orion constellation as documented in a paper by Nottingham Trent Univesity on "The Orion constellation as an installation" found [here](https://arxiv.org/ftp/arxiv/papers/1110/1110.3469.pdf).
# 
# Spend some time looking at `x`, `y`, and `z`, does each fall within a range?

# In[2]:


# Orion
x = [-0.41, 0.57, 0.07, 0.00, -0.29, -0.32,-0.50,-0.23, -0.23]
y = [4.12, 7.71, 2.36, 9.10, 13.35, 8.13, 7.19, 13.25,13.43]
z = [2.06, 0.84, 1.56, 2.07, 2.36, 1.72, 0.66, 1.25,1.38]


# ## 3. Create a 2D Visualization
# 
# Before we visualize the stars in 3D, let's get a sense of what they look like in 2D. 
# 
# Create a figure for the 2d plot and save it to a variable name `fig`. (hint: `plt.figure()`)
# 
# Add your subplot `.add_subplot()` as the single subplot, with `1,1,1`.(hint: `add_subplot(1,1,1)`)
# 
# Use the scatter [function](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html) to visualize your `x` and `y` coordinates. (hint: `.scatter(x,y)`)
# 
# Render your visualization. (hint: `plt.show()`)
# 
# Does the 2D visualization look like the Orion constellation we see in the night sky? Do you recognize its shape in 2D? There is a curve to the sky, and this is a flat visualization, but we will visualize it in 3D in the next step to get a better sense of the actual star positions. 

# In[3]:


fig = plt.figure(figsize=(10,20))
fig.add_subplot(1,1,1)
plt.scatter(x,y, color='blue')

plt.title("Orion Constellation in 2D")
plt.show()


# ## 4. Create a 3D Visualization
# 
# Create a figure for the 3D plot and save it to a variable name `fig_3d`. (hint: `plt.figure()`)
# 
# 
# Since this will be a 3D projection, we want to make to tell Matplotlib this will be a 3D plot.  
# 
# To add a 3D projection, you must include a the projection argument. It would look like this:
# ```py
# projection="3d"
# ```
# 
# Add your subplot with `.add_subplot()` as the single subplot `1,1,1` and specify your `projection` as `3d`:
# 
# `fig_3d.add_subplot(1,1,1,projection="3d")`)
# 
# Since this visualization will be in 3D, we will need our third dimension. In this case, our `z` coordinate. 
# 
# Create a new variable `constellation3d` and call the scatter [function](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html) with your `x`, `y` and `z` coordinates. 
# 
# Include `z` just as you have been including the other two axes. (hint: `.scatter(x,y,z)`)
# 
# Render your visualization. (hint `plt.show()`.)
# 

# In[4]:


fig_3d = plt.figure(figsize=(10,10))
ax = fig_3d.add_subplot(1,1,1, projection='3d')
constellation3d = plt.plot(x,y,z)
plt.title("Orion in 3D")
plt.show()


# ## 5. Rotate and explore
# 
# Use your mouse to click and drag the 3D visualization in the previous step. This will rotate the scatter plot. As you rotate, can you see Orion from different angles? 
# 
# Note: The on and off button that appears above the 3D scatter plot allows you to toggle rotation of your 3D visualization in your notebook.
# 
# Take your time, rotate around! Remember, this will never look exactly like the Orion we see from Earth. The visualization does not curve as the night sky does.
# There is beauty in the new understanding of Earthly perspective! We see the shape of the warrior Orion because of Earth's location in the universe and the location of the stars in that constellation.
# 
# Feel free to map more stars by looking up other celestial x, y, z coordinates [here](http://www.stellar-database.com/).
# 

# In[6]:


#test data from starcharts
x_values=[0.994772,0.97249,0.435119,0.998442,0.998448,0.873265,0.512379,0.949168,0.882312,0.69724,0.980198,0.693047,0.135171,0.962619,
0.883455,0.816743,0.963482,0.752989,0.936549,0.943971,0.986062,0.987091,0.77846,0.621566,0.798325,0.719465,0.984616,0.422933,0.985806,
0.785002,0.346752,0.870924,0.935111,0.96779,0.972523,0.777474]
y_values=[0.023164,0.024187,0.012234,0.033711,0.035746,0.031968,0.020508,0.037455,0.036017,0.028641,0.042952,0.031231,0.005924,0.047354,
0.044652,0.041844,0.055705,0.044458,0.059751,0.060384,0.064542,0.071481,0.058165,0.048148,0.063981,0.058843,0.083667,0.037061,0.088838,
0.072548,0.031329,0.082019,0.089096,0.094996,0.097324,0.08183]
z_values=[-0.099456,0.231685,0.90029,-0.044468,-0.042707,0.486196,0.858515,0.312534,-0.469285,-0.716265,0.193306,0.720216,-0.990805,
-0.266689,-0.466383,-0.575482,0.261913,0.656529,0.345408,-0.324457,0.153349,0.143323,0.624993,0.781881,0.598819,0.692032,-0.153397,   
-0.905403,0.142461,0.615231,-0.937433,-0.484524,-0.342971,0.233147,-0.211488,0.623569]

#make the figure
fig_3d = plt.figure(figsize=(10,10))
ax = fig_3d.add_subplot(1,1,1, projection='3d')
constellation3d = plt.plot(x_values,y_values,z_values)
plt.show()

