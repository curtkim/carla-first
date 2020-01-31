import carla
import random
import time

def main():
    with open('Town01.xodr', 'r') as file:
        data = file.read()
        #print(data)
        map = carla.Map("Town01", data)

        print(map.transform_to_geolocation(carla.Location(0,0,0)))
        wp1 = map.get_waypoint(carla.Location(0,0,0))
        print(wp1)
        print(wp1.next(10)[0])

        topo = map.get_topology()
        for (a, b) in topo:
            print(a.transform.location.distance(b.transform.location), a, b)

if __name__ == '__main__':
    main()
