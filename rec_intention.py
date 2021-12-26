from natasha import (Segmenter,
                     NewsNERTagger,
                     NewsEmbedding,
                     NewsMorphTagger,
                     NewsSyntaxParser,
                     Doc, LOC, MorphVocab, DatesExtractor)
import error_processing
from state import state

segmenter = Segmenter()
emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
morph_vocab = MorphVocab()
ner_tagger = NewsNERTagger(emb)
dates_extractor = DatesExtractor(morph_vocab)

spb = ['санкт-петербург', 'питер', 'спб', 'петербург']
msk = ['москва', 'мск']
days = ['сегодня', 'завтра', 'сейчас']


def get_city(text):
    doc = Doc(text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    doc.tag_ner(ner_tagger)
    for span in doc.spans:
        span.normalize(morph_vocab)

    location = [_.normal for _ in doc.spans if _.type == LOC]
    if len(location) == 0:
        return None

    if str(location[0]).lower() in spb:
        return 'spb'
    elif str(location[0]).lower() in msk:
        return 'msk'
    return None


def get_day(text):
    for i in text.split(' '):
        if i in days:
            return i
    return None


def rec_intention(text, chat_id, bot):
    if state['city'] is None:
        city = get_city(text)
        state['city'] = city

    if state['day'] is None:
        day = get_day(text)
        state['day'] = day

    if state['city'] is None and state['day'] is None:
        error_processing.error_processing('none_data', chat_id, bot)
    elif state['city'] is None:
        error_processing.error_processing('unsupported_city', chat_id, bot)
    elif state['day'] is None:
        error_processing.error_processing('unsupported_day', chat_id, bot)
    return state
