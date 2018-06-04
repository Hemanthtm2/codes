#!/usr/bin/python 

import facebook

token = 'EAACEdEose0cBALd8bYJayZBJMnyErKbU9pqbbI3Oh5seQi7TfEpTyHfmtFq3WJvajxRpzBKNqU6mCehOVi2EPBx2lUWbOWcy23ZALasb4JBcpMhUvHmL6QZCxM2AJIL6y23WNSGLnZBuE5dmwTgR788n5s5Dv0I7F3iX1e1ubT38Wu1eU9oqboyATfqnIZBXaGyxTccNWvgZDZD'
graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
friend_list = [friend['name'] for friend in friends['data']]
print friend_list
