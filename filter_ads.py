def filter_ads(ads: list) -> list[dict]:
    with open("sent_ads.txt", "rt") as f:
        current_links = f.read().splitlines()

    return_list = []

    for ad in ads:
        ad_link = ad["link"]
        if ad_link in current_links:
            continue

        return_list.append(ad)

        with open("sent_ads.txt", "a") as f:
            f.write(ad_link)
            f.write("\n")

    return return_list
