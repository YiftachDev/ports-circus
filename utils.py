

def handle_messages(data: str):
    data_splited = data.split(" ")
    msg, port = data_splited[0], data_splited[1]
    return msg, port


def create_msg(data) -> str:
    """
    Create a valid protocol message, with length field
    """
    str_data = str(data)
    length = str(len(str_data)).zfill(4)
    msg = length + str_data
    return msg


def get_msg(my_socket):
    """
    Extract message from protocol, without the length field
    If length field does not include a number, returns False, "Error"
    """
    length = my_socket.recv(4).decode()
    try:
        length = int(length)
    except:
        return False, "Error"
    msg = my_socket.recv(length).decode()
    return True, msg