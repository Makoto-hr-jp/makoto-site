export class OdgovorModel {
  public gradivo: number;
  public listic: number;
  public zadaca: number;
  public komentar: string;

  constructor(gradivo: number, listic: number, zadaca: number, komentar: string) {
    this.gradivo = gradivo;
    this.listic = listic;
    this.zadaca = zadaca;
    this.komentar = komentar;
  }
}
