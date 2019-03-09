export class PitanjeOdgovorModel {
  public pitanje: string;
  public odgovori: string[];


  constructor(pitanje: string, odgovori: string[]) {
    this.pitanje = pitanje;
    this.odgovori = odgovori;
  }
}
