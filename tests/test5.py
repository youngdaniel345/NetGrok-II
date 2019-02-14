import sqlite3

conn = sqlite3.connect('netgrok.db')
print "Opened database successfully";

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (0, '192.168.1.1', '7188', '162.221.202.8', '443', '2018-10-10 15:49:32', '2018-10-10 15:49:33', '364', '836', 'HTTPS', 'google.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (1, '192.168.1.1', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'amazon.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (2, '192.168.1.2', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'amazon.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (3, '192.168.1.3', '7188', '162.221.202.8', '443', '2018-10-10 15:49:32', '2018-10-10 15:49:33', '364', '836', 'HTTPS', 'twitter.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (4, '192.168.1.4', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'cnn.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (5, '192.168.1.5', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'facebook.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (6, '192.168.1.2', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'facebook.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (7, '192.168.1.3', '7188', '162.221.202.8', '443', '2018-10-10 15:49:32', '2018-10-10 15:49:33', '364', '836', 'HTTPS', 'twitter.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (8, '192.168.1.4', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'apple.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (9, '192.168.1.5', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'yahoo.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (10, '192.168.1.5', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'yahoo.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (11, '192.168.1.5', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'yahoo.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (12, '192.168.1.5', '7188', '162.221.202.8', '443', '2018-10-10 15:49:32', '2018-10-10 15:49:33', '364', '836', 'HTTPS', 'google.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (13, '192.168.1.6', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'msn.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (14, '192.168.1.7', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'msn.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (15, '192.168.1.8', '7188', '162.221.202.8', '443', '2018-10-10 15:49:32', '2018-10-10 15:49:33', '364', '836', 'HTTPS', 'msn.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (16, '192.168.1.9', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'cnn.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (17, '192.168.1.10', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'facebook.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (18, '192.168.1.11', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'facebook.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (19, '192.168.1.12', '7188', '162.221.202.8', '443', '2018-10-10 15:49:32', '2018-10-10 15:49:33', '364', '836', 'HTTPS', 'twitter.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (20, '192.168.1.13', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'apple.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (21, '192.168.1.14', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'yahoo.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (22, '192.168.1.15', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'yahoo.com')");

conn.execute("INSERT INTO NETGROK (ID, SRC_IP, SRC_PORT, DST_IP, DST_PORT, TIME_START, TIME_END, DOWNLOAD, UPLOAD, PROTOCOL, HOST) \
      VALUES (23, '192.168.1.16', '7188', '162.221.202.8', '443', '2018-10-10 15:49:34', '2018-10-10 15:49:36', '364', '836', 'HTTPS', 'yahoo.com')");

conn.commit()
conn.close()
