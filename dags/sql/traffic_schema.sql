CREATE TABLE IF NOT EXISTS traffic_data(
    "track_id" SERIAL NOT NULL,      
    "type" TEXT NOT NULL,       
    "traveled_d" TEXT NOT NULL,   
    "avg_speed"  TEXT NOT NULL,   
    "lat"   TEXT NOT NULL,        
    "lon"  TEXT NOT NULL,         
    "speed"  TEXT NOT NULL,       
    "lon_acc" TEXT NOT NULL,      
    "lat_acc"  TEXT NOT NULL,     
    "time"  TEXT NOT NULL,        
)