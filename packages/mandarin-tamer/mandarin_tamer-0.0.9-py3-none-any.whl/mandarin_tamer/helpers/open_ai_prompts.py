import json

from openai import OpenAI

client = OpenAI()


def openai_s2t_one2many_mappings(sentence, token, mapping_dict):
    return _one2many_mapping(
        "replacing Simplified Mandarin with Traditional Taiwanese Mandarin",
        "sentence",
        sentence,
        token,
        mapping_dict,
    )


def openai_t2s_one2many_mappings(tokenized_sentence, token, mapping_dict):
    return _one2many_mapping(
        "replacing Traditional Mandarin with Simplified Mandarin",
        "tokenized_sentence",
        tokenized_sentence,
        token,
        mapping_dict,
    )


def openai_modernize_simp_one2many_mappings(tokenized_sentence, token, mapping_dict):
    return _one2many_mapping(
        "replacing outdated/archaic Simplified Mandarin with Modern Simplified Mandarin",
        "tokenized_sentence",
        tokenized_sentence,
        token,
        mapping_dict,
    )


def openai_normalize_simp_one2many_mappings(tokenized_sentence, token, mapping_dict):
    return _one2many_mapping(
        "replacing uncommon words with more common equivalents in Simplified Mandarin",
        "tokenized_sentence",
        tokenized_sentence,
        token,
        mapping_dict,
    )


def openai_modernize_trad_one2many_mappings(tokenized_sentence, token, mapping_dict):
    return _one2many_mapping(
        "replacing outdated/archaic Traditional Mandarin with Modern Traditional Mandarin",
        "tokenized_sentence",
        tokenized_sentence,
        token,
        mapping_dict,
    )


def openai_normalize_trad_one2many_mappings(tokenized_sentence, token, mapping_dict):
    return _one2many_mapping(
        "replacing uncommon words with more common equivalents in Traditional Mandarin",
        "tokenized_sentence",
        tokenized_sentence,
        token,
        mapping_dict,
    )


def openai_taiwanize_one2many_mappings(tokenized_sentence, token, mapping_dict):
    return _one2many_mapping(
        "replacing Traditional Mandarin with Traditional Taiwanese Mandarin",
        "tokenized_sentence",
        tokenized_sentence,
        token,
        mapping_dict,
    )


def openai_detaiwanize_one2many_mappings(tokenized_sentence, token, mapping_dict):
    return _one2many_mapping(
        "replacing Traditional Taiwanese Mandarin with Traditional Hong Kong Mandarin",
        "tokenized_sentence",
        tokenized_sentence,
        token,
        mapping_dict,
    )


def _one2many_mapping(prompt_intent, sentence_label, sentence, token, mapping_dict):
    system_context = f"""
    Return as json the best_replacement_token for the token in the sentence based on the options in the mapping_dictionary for {prompt_intent}.
    """
    user_context = f"{sentence_label}: {sentence}; token: {token}; mapping_dictionary: {mapping_dict}"
    response = (
        get_openai_response(
            system_content=system_context,
            user_content=user_context,
            json_mode=True,
        )
        or '{"best_replacement_token": ""}'
    )
    json_response = json.loads(response)
    return json_response["best_replacement_token"]


def get_openai_response(
    system_content=None,
    user_content=None,
    assistant_content=None,
    json_mode=False,
    max_tokens=3500,
    temperature=0,
):
    messages = []
    if system_content:
        messages.append({"role": "system", "content": system_content})
    if user_content:
        messages.append({"role": "user", "content": user_content})
    if assistant_content:
        messages.append({"role": "assistant", "content": assistant_content})

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"} if json_mode else {"type": "text"},
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0,
    )
    return completion.choices[0].message.content
