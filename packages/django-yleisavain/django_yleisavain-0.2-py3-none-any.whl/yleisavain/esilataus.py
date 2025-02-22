# -*- coding: utf-8 -*-

import functools
from typing import Iterable

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Esilataus(models.Prefetch):
  '''
  Laajennettu, sisältötyyppikohtainen
  GenericForeignKey-yleisavaimeen liittyvien rivien esilatausluokka.
  '''
  def __init__(self, lookup: str, qss: Iterable[models.QuerySet], **kwargs):
    super().__init__(lookup, **kwargs)
    self.tyypit_ja_kyselyt: dict[ContentType, models.QuerySet] = {
      tyyppi: next(qs for qs in qss if qs.model == malli)
      for malli, tyyppi
      in ContentType.objects.get_for_models(*(qs.model for qs in qss)).items()
    }
    # def __init__

  def __repr__(self):
    return (
      f'<Esilataus {self.prefetch_through!r}:'
      f' {", ".join((repr(malli.model) for malli in self.tyypit_ja_kyselyt))}>'
    )

  # class Esilataus


def aseta(kohde):
  ''' Koriste: aseta funktio annetun luokan määreeksi ja palauta. '''
  return lambda maare: (
    setattr(kohde, nimi := maare.__name__, maare)
    or getattr(kohde, nimi)
  )
  # def aseta


# Puukota tulosten esilatausfunktio huomioimaan yllä määritellyt Esilataukset.
@aseta(models.query)
@functools.wraps(models.query.prefetch_one_level)
def prefetch_one_level(instances, prefetcher, lookup, level):
  # pylint: disable=protected-access

  # Puukota sisältötyypin haku tarvittaessa.
  if all((
    isinstance(lookup, Esilataus),
    isinstance(prefetcher, GenericForeignKey),
  )):
    @aseta(prefetcher)
    @functools.wraps(prefetcher.get_content_type)
    def get_content_type(**kwargs):
      ct = get_content_type.__wrapped__(**kwargs)

      # Puukota sisältötyypin tietueiden haku.
      @aseta(ct)
      @functools.wraps(ct.get_all_objects_for_this_type)
      def get_all_objects_for_this_type(**kwargs2):

        # Mikäli tämäntyyppinen kyselyjoukko on määritetty, käytetään sitä.
        # Muussa tapauksessa ajetaan oletustoteutus.
        try:
          kysely = lookup.tyypit_ja_kyselyt[ct]
        except KeyError:
          return get_all_objects_for_this_type.__wrapped__(**kwargs2)
        else:
          return kysely.using(ct._state.db).filter(**kwargs2)
        # def get_all_objects_for_this_type

      return ct
      # def get_content_type

    # if all

  return prefetch_one_level.__wrapped__(instances, prefetcher, lookup, level)
  # def prefetch_one_level
