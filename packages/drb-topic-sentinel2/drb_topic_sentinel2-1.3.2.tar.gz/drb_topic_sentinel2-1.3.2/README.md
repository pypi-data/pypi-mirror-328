# drb-topic-sentinel2
The `drb-topic-sentinel2` is a DRB plugin declaring topics about
[Sentinel-2](https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2)
EO satellite.

## Installation
```bash
pip install drb-topic-sentinel2
```

## Sentinel-2 Topics
This section references topics defined in the `drb-topic-sentinel2` DRB plugin.



```mermaid
graph TB
    subgraph "drb-topic-safe"
        A([SAFE Product<br/>487b0c70-6199-46de-9e41-4914520e25d9])
    end
    
    subgraph "drb-topic-sentinel2"
        E([Sentinel-2 Product<br/>329762ec-e1a8-11ec-8fea-0242ac120002])
        B([Sentinel-2 User Product<br/>e0750a16-f302-11ec-b939-0242ac120002])
        C([Sentinel-2 Product Data Item<br/>8351f100-c0c1-11ec-9d64-0242ac120002])
        D([Sentinel-2 Aux<br/>02318e52-fd2d-11ec-b939-0242ac120002])
    end

    B --> A
    C & D --> E
```
### Sentinel-2 Aux products Topics

```mermaid
graph RL
    subgraph "drb-topic-sentinel2"
        A([Sentinel-2 Aux<br/>02318e52-fd2d-11ec-b939-0242ac120002])
        B([Sentinel-2 AUX SAD product<br/>be45c266-f23d-11ec-b939-0242ac120002])
        C([Sentinel-2 AUX ECMWFD<br/>060054d6-f23e-11ec-b939-0242ac120002])
        D([Sentinel-2 AUX UT1UTC<br/>dc74378e-f23f-11ec-b939-0242ac120002])
        E([Sentinel-2 AUX RESORB<br/>67c1abf6-f2ee-11ec-b939-0242ac120002])
        F([Sentinel-2 AUX PREORB<br/>6d1db586-f2ee-11ec-b939-0242ac120002])
        G([Sentinel-2 AUX GIP product<br/>060054d6-f23e-11ec-b939-0242ac120002])
        H([Sentinel-2 AUX ECMWFD & UT1UTC product<br/>20cacd114-0c20-11ed-861d-0242ac120002])
        I([Sentinel-2 AUX RESORB & PREORB product<br/>8bc2ca58-0c25-11ed-861d-0242ac120002])
        J([Sentinel-2 HDR file<br/>afbe3414-0c1c-11ed-861d-0242ac120002])
    end
     
    B & H & I & G  --> A
    D & C --> H
    E & F --> I
```

### Sentinel-2 User products Topics

```mermaid
graph BT
    subgraph "drb-topic-safe"
        A([SAFE Product<br/>487b0c70-6199-46de-9e41-4914520e25d9])
    end
    
    subgraph "drb-topic-sentinel2"
        B([Sentinel-2 User Product<br/>e0750a16-f302-11ec-b939-0242ac120002])
        C([Sentinel-2 User Product Level-0<br/>bc7a2008-e1ad-11ec-8fea-0242ac120002])
        D([Sentinel-2 User Product Level-1A<br/>96b1dd4c-e1ae-11ec-8fea-0242ac120002])
        E([Sentinel-2 User Product Level-1B<br/>da832a58-e1ae-11ec-8fea-0242ac120002])
        F([Sentinel-2 User Product Level-1C<br/>242ce8e2-e1af-11ec-8fea-0242ac120002])
        G([Sentinel-2 User Product Level-2A<br/>73b017d6-e1af-11ec-8fea-0242ac120002])
    end
    
    B --> A
    C & D & E & F & G --> B
```


### Sentinel-2 PDI products Topics

```mermaid
graph BT  
    subgraph "drb-topic-sentinel2"
        A([Sentinel-2 Product<br/> 329762ec-e1a8-11ec-8fea-0242ac120002])
        B([Sentinel-2 PDI<br/>172f47a2-f307-11ec-b939-0242ac120002])
        C([Sentinel-2 Level-0 Granules and Datastrip package<br/>3d70f9a4-fd3b-11ec-b939-0242ac120002])
        D([Sentinel-2 Level-1C Tile Image File<br/>ff9720b6-f2f1-11ec-b939-0242ac120002])
        E([Sentinel-2 Level-1C Tile Image File exotic<br/>03a7dc7c-f2f2-11ec-b939-0242ac120002])
        F([Sentinel-2 Level-0 HKTM<br/>3f43fa3e-f2f9-11ec-b939-0242ac120002])
    end
    
    B & F--> A
    C & D & E  --> B
```

### Sentinel-2 Granule products Topics

```mermaid
graph RL  
    subgraph "drb-topic-sentinel2"
        A([Sentinel-2 Product<br/> 329762ec-e1a8-11ec-8fea-0242ac120002])
        B([Sentinel-2 Granule<br/>c6da0d68-f23a-11ec-b939-0242ac120002])
        C([Sentinel-2 Level-0 Granule<br/>3ed2f5ba-f23a-11ec-b939-0242ac120002])
        D([Sentinel-2 Level-0 Granule tar<br/>aed3f1e8-0bf8-11ed-861d-0242ac120002])
        E([Sentinel-2 Level-1A Granule<br/>beadaaac-f2f6-11ec-b939-0242ac120002])
        F([Sentinel-2 Level-1A Granule tar<br/>bec4dfb8-0bf8-11ed-861d-0242ac120002])
        G([Sentinel-2 Level-1B Granule<br/>c4018b4a-f2f6-11ec-b939-0242ac120002])
        H([Sentinel-2 Level-1B Granule tar<br/>defc1e86-0bf8-11ed-861d-0242ac120002])
        I([Sentinel-2 Level-1C Granule<br/>c7327bd0-f2f6-11ec-b939-0242ac120002])
        J([Sentinel-2 Level-1C Granule tar<br/>e9d52d0c-0bf8-11ed-861d-0242ac120002])
        K([Sentinel-2 Level-2A Granule<br/>c9c726c0-f2f6-11ec-b939-0242ac120002])
        L([Sentinel-2 Level-2A Granule tar<br/>116c5804-0bf9-11ed-861d-0242ac120002])
    end
    
    B --> A
    C & D & E & F & G & H & I & J & K & L --> B
```

### Sentinel-2 DataStrip products Topics

```mermaid
graph RL  
    subgraph "drb-topic-sentinel2"
        A([Sentinel-2 Product<br/> 329762ec-e1a8-11ec-8fea-0242ac120002])
        B([Sentinel-2 Datastrip<br/>fad132d2-f2fc-11ec-b939-0242ac120002])
        C([Sentinel-2 Level-0 Datastrip<br/>040e4f2e-f2fd-11ec-b939-0242ac120002])
        D([Sentinel-2 Level-0 Datastrip tar<br/>746dc578-0bf4-11ed-861d-0242ac120002])
        E([Sentinel-2 Level-1A Datastrip<br/>05d83572-f2fd-11ec-b939-0242ac120002])
        F([Sentinel-2 Level-1A Datastrip tar<br/>3f1ab53c-0bf6-11ed-861d-0242ac120002])
        G([Sentinel-2 Level-1B Datastrip<br/>081aa2a2-f2fd-11ec-b939-0242ac120002])
        H([Sentinel-2 Level-1B Datastrip tar<br/>4784eb66-0bf6-11ed-861d-0242ac120002])
        I([Sentinel-2 Level-1C Datastrip<br/>0a57ea48-f2fd-11ec-b939-0242ac120002])
        J([Sentinel-2 Level-1C Datastrip tar<br/>50448cde-0bf6-11ed-861d-0242ac120002])
        K([Sentinel-2 Level-2A Datastrip<br/>0cbf0d70-f2fd-11ec-b939-0242ac120002])
        L([Sentinel-2 Level-2A Datastrip tar<br/>564d3d42-0bf6-11ed-861d-0242ac120002])
    end
    
    B --> A
    C & D & E & F & G --> B
```