import {PitanjeOdgovorModel} from './pitanje-odgovor.model';

export class AnketaModel {
  public pitanjaOdgovori: PitanjeOdgovorModel[];


  constructor(pitanjaOdgovori: PitanjeOdgovorModel[]) {
    this.pitanjaOdgovori = pitanjaOdgovori;
  }
}
