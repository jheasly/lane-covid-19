# OHA counts *always* lags Lane County daily case counts ...
lane_count_fixes = (
    ('2020-07-18', 40,),
    ('2020-07-20', 5,),
    ('2020-07-21', 7,),
    ('2020-07-23', 7,),
    ('2020-07-24', 18,),
    ('2020-07-25', 4,),
    ('2020-07-26', 9,),
    ('2020-07-27', 8,),
    ('2020-07-31', 19,),
    ('2020-08-01', 12,),
    ('2020-08-02', 3,),
    ('2020-08-03', 10,),
    ('2020-08-04', 8,),
    ('2020-08-05', 7,),
    ('2020-08-06', 9,),
    ('2020-08-07', 18,),
    ('2020-08-08', 10,),
    ('2020-08-09', 9,),
    ('2020-08-10', 1,),
    ('2020-08-11', 7,),
    ('2020-08-12', 9,),
    ('2020-08-13', 5,),
    ('2020-08-14', 9,),
    ('2020-08-15', 3,),
    ('2020-08-16', 2,),
    ('2020-08-17', 5,),
    ('2020-08-18', 7,),
    ('2020-08-19', 4,),
    ('2020-08-20', 2,),
    ('2020-08-21', 5,),
    ('2020-08-22', 6,),
    ('2020-08-23', 2,),
    ('2020-08-24', 2,),
    ('2020-08-25', 3,),
    ('2020-08-26', 6,),
    ('2020-08-28', 18,),
    ('2020-08-29', 10,),
    ('2020-08-30', 4,),
    ('2020-08-31', 13,),
    ('2020-09-02', 11,),
    ('2020-09-03', 13,),
    ('2020-09-04', 22,),
    ('2020-09-05', 4,),
    ('2020-09-06', 13,),
    ('2020-09-08', 6,),
    ('2020-09-09', 11,),
    ('2020-09-10', 4,),
    ('2020-09-11', 11,),
    ('2020-09-12', 12,),
    ('2020-09-13', 5,),
    ('2020-09-14', 21,),
    ('2020-09-15', 11,),
    ('2020-09-16', 16,),
    ('2020-09-17', 23,),
    ('2020-09-18', 20,),
    ('2020-09-19', 10,),
    ('2020-09-20', 17,),
    ('2020-09-21', 45,),
    ('2020-09-22', 14,),
    ('2020-09-23', 48,),
    ('2020-09-24', 47,),
    ('2020-09-25', 46,),
    ('2020-09-26', 39,),
    ('2020-09-27', 21,),
    ('2020-09-28', 15,),
    ('2020-09-29', 37,),
    ('2020-09-30', 34,),
    ('2020-10-01', 18,),
    ('2020-10-02', 58,),
    ('2020-10-03', 74,),
    ('2020-10-04', 30,),
    ('2020-10-05', 26,),
    ('2020-10-06', 54,),
    ('2020-10-07', 63,),
    ('2020-10-08', 40,),
    ('2020-10-09', 50,),
    ('2020-10-10', 68,),
    ('2020-10-11', 29,),
    ('2020-10-12', 26,),
    ('2020-10-13', 29,),
    ('2020-10-14', 63,),
    ('2020-10-15', 21,),
    ('2020-10-16', 82,),
    ('2020-10-17', 43,),
    ('2020-10-18', 24,),
    ('2020-10-19', 35,),
    ('2020-10-20', 39,),
    ('2020-10-21', 40,),
    ('2020-10-22', 20,),
    ('2020-10-23', 71,),
    ('2020-10-24', 26,),
    ('2020-10-25', 43,),
    ('2020-10-26', 12,),
    ('2020-10-27', 26,),
    ('2020-10-28', 35,),
    ('2020-10-29', 13,),
    ('2020-10-30', 35,),
    ('2020-10-31', 72,),
    ('2020-11-01', 31,),
    ('2020-11-02', 2,),
    ('2020-11-03', 27,),
    ('2020-11-04', 23,),
    ('2020-11-05', 37,),
    ('2020-11-06', 73,),
    ('2020-11-07', 69,),
    ('2020-11-08', 48,),
    ('2020-11-09', 13,),
    ('2020-11-10', 44,),
    ('2020-11-11', 73,),
    ('2020-11-12', 43,),
    ('2020-11-13', 83,),
    ('2020-11-14', 96,),
    ('2020-11-15', 31,),
    ('2020-11-16', 37,),
    ('2020-11-17', 82,),
    ('2020-11-18', 114,),
    ('2020-11-19', 97,),
    ('2020-11-20', 103,),
    ('2020-11-21', 80,),
    ('2020-11-22', 73,),
    ('2020-11-23', 60,),
    ('2020-11-24', 88,),
    ('2020-11-25', 92,),
    ('2020-11-29', 77,),
    ('2020-11-30', 44,),
    ('2020-12-01', 76,),
    ('2020-12-02', 88,),
    ('2020-12-03', 64,),
    ('2020-12-04', 111,),
    ('2020-12-05', 138,),
    ('2020-12-06', 113,),
    ('2020-12-07', 51,),
    ('2020-12-08', 105,),
    ('2020-12-09', 86,),
    ('2020-12-10', 77,),
    ('2020-12-11', 131,),
    ('2020-12-12', 80,),
    ('2020-12-13', 99,),
    ('2020-12-14', 28,),
    ('2020-12-15', 117,),
    ('2020-12-16', 118,),
    ('2020-12-17', 32,),
    ('2020-12-18', 128,),
    ('2020-12-19', 153,),
    ('2020-12-20', 58,),
    ('2020-12-21', 36,),
    ('2020-12-22', 60,),
    ('2020-12-23', 103,),
    ('2020-12-24', 32,),
    ('2020-12-25', 57,),
    ('2020-12-26', 104,),
    ('2020-12-27', 29,),
    ('2020-12-28', 24,),
    ('2020-12-29', 45,),
    ('2020-12-30', 106,),
    ('2020-12-31', 109,),
    ('2021-01-01', 71,),
    ('2021-01-02', 122,),
    ('2021-01-03', 57,),
    ('2021-01-04', 35,),
    ('2021-01-05', 61,),
    ('2021-01-06', 60,),
    ('2021-01-07', 106,),
    ('2021-01-08', 65,),
    ('2021-01-09', 143,),
    ('2021-01-10', 84,),
    ('2021-01-11', 30,),
    ('2021-01-12', 103,),
    ('2021-01-13', 112,),
    ('2021-01-14', 61,),
    ('2021-01-15', 86,),
    ('2021-01-16', 103,),
    ('2021-01-17', 54,),
    ('2021-01-18', 68,),
    ('2021-01-19', 72,),
    ('2021-01-20', 42,),
    ('2021-01-21', 101,),
    ('2021-01-22', 85,),
    ('2021-01-23', 70,),
    ('2021-01-24', 52,),
    ('2021-01-25', 37,),
    ('2021-01-26', 38,),
    ('2021-01-27', 49,),
    ('2021-01-28', 71,),
    ('2021-01-29', 62,),
    ('2021-01-30', 59,),
    ('2021-01-31', 54,),
    ('2021-02-01', 53,),
    ('2021-02-02', 27,),
    ('2021-02-03', 117,),
    ('2021-02-04', 77,),
    ('2021-02-05', 41,),
    ('2021-02-06', 79,),
    ('2021-02-07', 16,),
    ('2021-02-08', 30,),
    ('2021-02-09', 25,),
    ('2021-02-10', 47,),
    ('2021-02-11', 57,),
    ('2021-02-12', 40,),
    ('2021-02-13', 50,),
    ('2021-02-14', 32,),
    ('2021-02-15', 36,),
    ('2021-02-16', 9,),
    ('2021-02-17', 38,),
    ('2021-02-18', 41,),
    ('2021-02-19', 45,),
    ('2021-02-20', 28,),
    ('2021-02-21', 16,),
    ('2021-02-22', 8,),
    ('2021-02-23', 39,),
    ('2021-02-24', 31,),
    ('2021-02-25', 45,),
    ('2021-02-26', 37,),
    ('2021-02-27', 23,),
    ('2021-02-28', 27,),
    ('2021-03-01', 28,),
    ('2021-03-02', 23,),
    ('2021-03-03', 14,),
    ('2021-03-04', 22,),
    ('2021-03-05', 13,),
    ('2021-03-06', 25,),
    ('2021-03-07', 18,),
    ('2021-03-08', 1,),
    ('2021-03-09', 24,),
    ('2021-03-10', 7,),
    ('2021-03-11', 12,),
    ('2021-03-12', 11,),
    ('2021-03-13', 7,),
    ('2021-03-14', 12,),
    ('2021-03-15', 6,),
    ('2021-03-16', 10,),
    ('2021-03-17', 16,),
    ('2021-03-18', 12,),
    ('2021-03-19', 17,),
    ('2021-03-20', 18,),
    ('2021-03-21', 11,),
    ('2021-03-22', 12,),
    ('2021-03-23', 16,),
    ('2021-03-24', 29,),
    ('2021-03-25', 12,),
    ('2021-03-26', 34,),
    ('2021-03-27', 13,),
    ('2021-03-28', 28,),
    ('2021-03-29', 7,),
    ('2021-03-30', 14,),
    ('2021-03-31', 32,),
    ('2021-04-01', 46,),
    ('2021-04-02', 28,),
    ('2021-04-03', 39,),
    ('2021-04-04', 43,),
    ('2021-04-05', 34,),
    ('2021-04-06', 35,),
    ('2021-04-07', 27,),
    ('2021-04-08', 46,),
    ('2021-04-09', 76,),
    ('2021-04-10', 35,),
    ('2021-04-11', 46,),
    ('2021-04-12', 36,),
    ('2021-04-13', 40,),
    ('2021-04-14', 51,),
    ('2021-04-15', 75,),
    ('2021-04-16', 74,),
    ('2021-04-17', 84,),
    ('2021-04-18', 12,),
    ('2021-04-19', 65,),
    ('2021-04-20', 70,),
    ('2021-04-21', 76,),
    ('2021-04-22', 52,),
    ('2021-04-23', 75,),
    ('2021-04-24', 86,),
    ('2021-04-25', 37,),
    ('2021-04-26', 19,),
    ('2021-04-27', 67,),
    ('2021-04-28', 57,),
    ('2021-04-29', 59,),
    ('2021-04-30', 88,),
    ('2021-05-01', 64,),
    ('2021-05-02', 56,),
    ('2021-05-03', 56,),
    ('2021-05-04', 47,),
    ('2021-05-05', 43,),
    ('2021-05-06', 69,),
    ('2021-05-07', 76,),
    ('2021-05-08', 47,),
    ('2021-05-09', 55,),
    ('2021-05-10', 7,),
    ('2021-05-11', 50,),
    ('2021-05-12', 47,),
    ('2021-05-13', 48,),
    ('2021-05-14', 45,),
    ('2021-05-15', 37,),
    ('2021-05-16', 39,),
    ('2021-05-17', 26,),
    ('2021-05-18', 29,),
    ('2021-05-19', 21,),
    ('2021-05-20', 35,),
    ('2021-05-21', 39,),
    ('2021-05-22', 0,),
    ('2021-05-23', 0,),
    ('2021-05-24', 86,),    
    ('2021-05-25', 25,),    
    ('2021-05-26', 35,),    
    ('2021-05-27', 5,),
    ('2021-05-28', 0,),
    ('2021-05-29', 0,),
    ('2021-05-30', 20,),
    ('2021-05-31', 60,),
    ('2021-06-01', 31,),    
    ('2021-06-02', 14,),    
    ('2021-06-03', 21,),    
    ('2021-06-04', 38,),    
    ('2021-06-05', 0,),    
    ('2021-06-06', 0,),    
    ('2021-06-07', 56,),    
    ('2021-06-08', 27,),    
    ('2021-06-09', 9,),    
    ('2021-06-10', 30,),    
    ('2021-06-11', 4,),    
    ('2021-06-12', 0,),    
    ('2021-06-13', 0,),   
    ('2021-06-14', 32,),    
    ('2021-06-15', 26,),
    ('2021-06-16', 18,),
    ('2021-06-17', 33,),
    ('2021-06-18', 8,),
    ('2021-06-19', 0,),
    ('2021-06-20', 0,),
    ('2021-06-21', 46,),
    ('2021-06-22', 20,),
    ('2021-06-23', 6,),
    ('2021-06-24', 10,),
    ('2021-06-25', 15,),
    ('2021-06-26', 0,),
    ('2021-06-27', 0,),
    ('2021-06-28', 43,),
    ('2021-06-29', 28,),
    ('2021-06-30', 15,),
    ('2021-07-01', 17,),
    ('2021-07-02', 8,),
    ('2021-07-03', 0,),
    ('2021-07-04', 0,),
    ('2021-07-05', 0,),
    ('2021-07-06', 44,),
    ('2021-07-07', 10,),
    ('2021-07-08', 13,),
    ('2021-07-09', 3,),
    ('2021-07-10', 0,),
    ('2021-07-11', 0,),
    ('2021-07-12', 32,),
    ('2021-07-13', 25,),
    ('2021-07-14', 7,),
    ('2021-07-15', 21,),
    ('2021-07-16', 14,),
    ('2021-07-17', 0,),
    ('2021-07-18', 0,),
    ('2021-07-19', 84,),
    ('2021-07-20', 19,),
    ('2021-07-21', 10,),
    ('2021-07-22', 50,),
    ('2021-07-23', 72,),
    ('2021-07-24', 0,),
    ('2021-07-25', 0,),
    ('2021-07-26', 79,),
    ('2021-07-27', 97,),
    ('2021-07-28', 88,),
    ('2021-07-29', 45,),
    ('2021-07-30', 81,),
    ('2021-07-31', 0,),
    ('2021-08-01', 0,),
    ('2021-08-02', 306,),
    ('2021-08-03', 135,),
    ('2021-08-04', 95,),
    ('2021-08-05', 0,),
    ('2021-08-06', 160,),
    ('2021-08-07', 0,),
    ('2021-08-08', 0,),
    ('2021-08-09', 622,),
    ('2021-08-10', 264,),
    ('2021-08-11', 183,),
    ('2021-08-12', 240,),
    ('2021-08-13', 250,),
    ('2021-08-14', 0,),
    ('2021-08-15', 316,),
    ('2021-08-16', 295,),
    ('2021-08-17', 79,),
    ('2021-08-18', 276,),
    ('2021-08-19', 268,),
    ('2021-08-20', 241,),
    ('2021-08-21', 277,),
    ('2021-08-22', 94,),
    ('2021-08-23', 299,),
    ('2021-08-24', 178,),
    ('2021-08-25', 189,),
    ('2021-08-26', 219,),
    ('2021-08-27', 240,),
    ('2021-08-28', 212,),
    ('2021-08-29', 145,),
    ('2021-08-30', 139,),
    ('2021-08-31', 184,),
    ('2021-09-01', 201,),
    ('2021-09-02', 206,),
    ('2021-09-03', 216,),
    ('2021-09-04', 217,),
    ('2021-09-05', 0,),
    ('2021-09-06', 0,),
    ('2021-09-07', 394,),
    ('2021-09-08', 140,),
    ('2021-09-09', 225,),
    ('2021-09-10', 254,),
    ('2021-09-11', 0,),
    ('2021-09-12', 299,),
    ('2021-09-13', 88,),
)
