from toontown.toonbase.ToontownGlobals import *

spawnPoints = {
    OutdoorZone: [(-156.9, -118.9, 0.025),
         (-35.6, 86.0, 1.25),
         (116.8, 10.8, 0.104),
         (-35, 145.7, 0.025),
         (-198.8, -45.1, 0.025),
         (-47.1, -25.5, 0.809),
         (59.15, 34.8, 1.767),
         (-81.02, -72.2, 0.026),
         (-167.9, 124.5, 0.025),
         (-226.7, -27.6, 0.025),
         (-16.0, -108.9, 0.025),
         (18.0, 58.5, 5.919),
         (91.4, 127.8, 0.025),
         (-86.5, -75.9, 0.025),
         (-48.751, -32.3, 1.143)],
    GolfZone: [(60, -118, 0.026),
               (-18.7, -73.5, 0.026),
               (-96.1, -81.1, 0.026),
               (-49.129, 0.203, 0.026),
               (19.1, 60, 0.026),
               (30.7, -50.5, 0.026),
               (-26.1, -50.1, 0.026)],
    ToontownCentral: [(-59.9, -6.9, 0.84),
         (-90.6, -3.0, -0.75),
         (27.1, -93.5, 2.5),
         (94.2, 33.5, 4),
         (35.4, 43.1, 4),
         (67.1, 105.5, 2.5),
         (-99.15, -87.3407, 0.52499),
         (1.60586, -119.492, 3.025),
         (43.2026, -76.287, 3.025),
         (129.137, -61.9039, 2.525),
         (92.99, -158.399, 3.025),
         (111.749, -8.59927, 4.57466),
         (41.999, -30.2923, 4.025),
         (31.0649, -43.9149, 4.025),
         (10.0156, 105.218, 2.525),
         (46.9667, 169.143, 3.025),
         (100.68, 93.9896, 2.525),
         (129.285, 58.6107, 2.525),
         (-28.6272, 85.9833, 0.525),
         (-114.613, 86.1727, 0.525),
         (-132.528, 31.255, 0.025)],
    DonaldsDock: [(52.9072, -23.4768, -12.308),
         (35.3827, -51.9196, -12.308),
         (17.4252, -57.3107, -12.308),
         (-0.716054, -68.5, -12.308),
         (-29.0169, -66.8887, -12.308),
         (-63.492, -64.2191, -12.308),
         (-72.2423, -58.3686, -12.308),
         (-97.9602, -42.8905, -12.308),
         (-102.215, -34.1519, -12.308),
         (-102.978, -4.09065, -12.308),
         (-101.305, 30.6454, -12.308),
         (-45.0621, -21.0088, -12.308),
         (-11.4043, -29.0816, -12.308),
         (2.33548, -7.71722, -12.308),
         (-8.643, 33.9891, -12.308),
         (-53.224, 18.1293, -12.308),
         (-99.7225, -8.1298, -12.308),
         (-100.457, 28.351, -12.308),
         (-76.7946, 4.21199, -12.308),
         (-64.9137, 37.5765, -12.308),
         (-17.6075, 102.135, -12.308),
         (-23.4112, 127.777, -12.308),
         (-11.3513, 128.991, -12.308),
         (-14.1068, 83.2043, -12.308),
         (53.2685, 24.3585, -12.308),
         (41.4197, 4.35384, -12.308)],
    DaisyGardens: [(-49, 156, 0.0),
         (-59, 50, 0.0),
         (19, 16, 0.0),
         (76, 38, 1.1),
         (102, 121, 0.0),
         (69, 123, 0.0),
         (49, 105, 0.0),
         (24, 156, 0.0),
         (-27, 127, 0.0),
         (-56, 105, 0.0),
         (-40, 113, 0.0),
         (25, 114, 0.0),
         (-6, 84, 0.0),
         (19, 96, 0.0),
         (0, 114, 0.0),
         (-78, 157, 10.0),
         (-33.4, 218.2, 10.0),
         (57, 205, 10.0),
         (32, 77, 0.0),
         (-102, 101, 0.0)],
    MinniesMelodyland: [(118, -39, 3.3),
         (118, 1, 3.3),
         (112, -22, 0.8),
         (108, -74, -4.5),
         (110, -65, -4.5),
         (102, 23.5, -4.5),
         (60, -115, 6.5),
         (-5, -115, 6.5),
         (-64, -77, 6.5),
         (-77, -44, 6.5),
         (-76, 3, 6.5),
         (44, 76, 6.5),
         (136, -96, -13.5),
         (85, -6.7, -13.5),
         (60, -95, -14.5),
         (72, 60, -13.5),
         (-55, -23, -14.5),
         (-21, 47, -14.5),
         (-24, -75, -14.5)],
    TheBrrrgh: [(-108, 46, 6.2),
         (-111, 74, 6.2),
         (-126, 81, 6.2),
         (-74, -75, 3.0),
         (-136, -51, 3.0),
         (-20, 35, 6.2),
         (-55, 109, 6.2),
         (58, -57, 6.2),
         (-42, -134, 6.2),
         (-68, -148, 6.2),
         (-1, -62, 6.2),
         (25, 2, 6.2),
         (-133, 53, 6.2),
         (-99, 86, 6.2),
         (30, 63, 6.2),
         (-147, 3, 6.2),
         (-135, -102, 6.2),
         (35, -98, 6.2)],
    DonaldsDreamland: [(86, 69, -17.4),
         (34, -48, -16.4),
         (87, -70, -17.5),
         (-98, 99, 0.0),
         (51, 100, 0.0),
         (-45, -12, -15.0),
         (9, 8, -15.0),
         (-24, 64, -17.2),
         (-100, -99, 0.0),
         (21, -101, 0.0),
         (88, -17, -15.0),
         (32, 70, -17.4),
         (53, 35, -15.8),
         (2, -30, -15.5),
         (-40, -56, -16.8),
         (-28, 18, -15.0),
         (-34, -88, 0.0)]
}

archiSpawnPoints = {
    ToontownCentral: [(85.1, -109.4, 2.525),
                      (60.6, -59.8, 6.051),
                      (13.4, -136.8, 3.025),
                      (-42, -86.8, 0.525),],
    ToontownCentral + 1: [(76, 66.5, 4.025),
                          (138.7, 123.4, 3.025),
                          (-61.1, 23.43, -6.139),
                          (21.1, 43.75, 4.983)],
    DonaldsDock: [(-74.65, -74.92, 7.821),
                  (56.15, -83.5, 3.28),
                  (-24.3, -1.7, 5.763),
                  (71.9, -14.4, 5.692)],
    DonaldsDock + 1: [(-15, 186.25, 3.281),
                      (-108.87, 41.48, 7.831),
                      (-42.85, 89, 3.28),
                      (59.77, 63.8, 3.28)],
    DaisyGardens: [(-33.38, 33.2, 0.025),
                   (25.6, 12.77, 0.025),
                   (102.9, 96.5, 0.025),
                   (-102.6, 94.5, 0.025)],
    DaisyGardens + 1: [(-10.9, 195.7, 0.025),
                       (84.6, 160.16, 10.014),
                       (-60.4, 205.2, 10.025),
                       (-85, 161.6, 10.022)],
    MinniesMelodyland: [(136.83, -21.3, 7.471),
                        (105, 38.5, -4.5),
                        (62.18, -22.6, -13.475),
                        (89.5, -97.8, -13.475)],
    MinniesMelodyland + 1: [(3.9, -115.9, 6.525),
                            (-35.16, -111.36, 6.525),
                            (-73.15, 23.4, 6.525),
                            (-6.9, 76.4, 6.525)],
    TheBrrrgh: [(-33.3, 110.8, 6.192),
                (36.76, 67.24, 6.192),
                (-101.2, 101.6, 6.192),
                (-105, 42.42, 6.192)],
    TheBrrrgh + 1: [(-65.306,  113.390,  6.192),
                    (-25.55, -151.49, 6.192),
                    (29.2, -116.6, 6.192),
                    (50.57, -72.28, 6.192)],
    DonaldsDreamland: [(28.6, -40.4, -16.022),
                       (-56, -53.26, -16.635),
                       (-101.54, -101.16, 0.025),
                       (17.85, -102.15, 0.025)],
    DonaldsDreamland + 1: [(60.55, 69.31, -17.41),
                           (-100.5, 63.27, -9.027),
                           (-29, 101.1, 0.025),
                           (58.21, 101, 0.025)],
    OutdoorZone: [(-242.25, 5.9, 0.025),
                  (-179.96, -72.45, 0.025),
                  (-47.77, -130.95, 0.025),
                  (-41.45, 130.67, 2.862)],
    OutdoorZone + 1: [(21.4, 48.2, 9.193),
                      (66.53, 159.82, 0.025),
                      (115.77, 12.7, 0.151),
                      (90.7, -96.9, 0.025)],
    GoofySpeedway: [(28.14, -43.5, 0.093),
                    (-23.6, 14.9, -0.323),
                    (32.65, 9.32, -0.323),
                    (62.8, 12.3, 0.095)],
    GoofySpeedway + 1: [(1.07, -103, -0.011),
                        (75.144, -110.05, -0.699),
                        (-2.55, -184.26, -0.732),
                        (-74.3, -111.5, -0.71)],
    SellbotHQ: [(59.4, -195.64, -11.502),
                (-22, -227.24, -9.212),
                (-13.69, -163.6, -19.594),
                (27.45, -204.58, -19.594)],
    SellbotHQ + 1: [(91.44, -145.69, 0.304),
                    (-94.74, -162.62, 0.298),
                    (-28.92, -43.42, 10.096),
                    (9.6, -258.95, 0.287)],
    CashbotHQ: [(131.6, -451.81, -23.439),
                (100.704, -453.48, -23.439),
                (51.63, -392.8, -23.493),
                (181.458, -392.8, -23.493)],
    CashbotHQ + 1: [(180.5, 45.39, -23.493),
                    (155, 149.2, -23.555),
                    (67.27, 151, -23.555),
                    (42.8, 44.093, -23.493)],
    LawbotHQ: [(218.35, -219.14, -68.367),
               (212.46, -135.87, -68.367),
               (333.58, -149, -43.052),
               (337.41, -206.75, -42.784)],
    LawbotHQ + 1: [(-42.75, -246.77, -68.367),
                   (-26.56, -126.04, -68.367),
                   (-149.22, -146.88, -28.61),
                   (-173.91, -214.31, -15.273)],
    BossbotHQ: [(139.33, 134.1, 0.025),
                (79.13, 130.89, 0.28),
                (175.35, -9.6, 0.025),
                (100.133,  -119.420,  0.025)],
    BossbotHQ + 1: [(-52.46, -60.25, 0.025),
                    (-50.25, 44.79, 0.025),
                    (-23.79, 113.6, 0.025),
                    (46.1, 130.75, 0.28)],
}

healAmounts = {
    OutdoorZone: 0.15,
    GolfZone: 0.15,
    GoofySpeedway: 0.15,
    ToontownCentral: 0.15,
    DonaldsDock: 0.20,
    DaisyGardens: 0.25,
    MinniesMelodyland: 0.30,
    TheBrrrgh: 0.35,
    DonaldsDreamland: 0.40,
    SellbotHQ: 0,
    CashbotHQ: 0,
    LawbotHQ: 0,
    BossbotHQ: 0
}

# How often should we spawn treasures? lower = faster
HOOD_SPAWN_FREQUENCY = 10
# How many treasures is allowed in a hood?
HOOD_SPAWN_CAP = 8