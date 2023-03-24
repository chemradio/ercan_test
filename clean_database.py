def cleanup_link_database(filepath: str):
    file_to_delete = open(filepath, "w")
    file_to_delete.close()
