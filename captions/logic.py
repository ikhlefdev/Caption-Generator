def generate_caption(product, platform, tone, feature, cta_type):
    hashtag = f"#{product.replace(' ', '')} #{platform.replace(' ', '')} #{feature.replace(' ', '')}"
    match tone:
        case "excited":
            return f"Get ready for the ultimate {product} experience on {platform}! This {feature} {product} is a game-changer. Don't miss out, {cta_type}! {hashtag}"
        case "neutral":
            return f"Check out the {product} on {platform}! This {feature} is a great addition. {cta_type}! {hashtag}"
        case "professional":
            return f"Introducing the {product} on {platform}. This {feature} {product} is designed for professionals. {cta_type} to learn more. {hashtag}"
        case _:
            return "Invalid tone selected"