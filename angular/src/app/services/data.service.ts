import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AnketaModel } from '../models/anketa.model';
import { FormGroup, FormControl, Validators } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private poll: AnketaModel;
  private url: string;
  private title: string;
  private serverResponse: any;
  pollForm: FormGroup = new FormGroup({});
  private httpOptions = {
	  headers: new HttpHeaders({
		'Content-Type':  'application/json'
	  })
  };

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    // this.getTemplate().subscribe( data => {
    //   this.poll = data['poll'];
    //   console.log("Anketa po modelu: ", this.poll);
    // });
    
  }

  getTemplate(): Observable<any> {
    return this.http.get('../../assets/files/template.json');
    // return this.http.get('../../assets/files/reshufled-template.json');
  }

  parseData() {
    this.pollForm.addControl('comment', new FormControl(''));
    this.getTemplate().subscribe( data => {
      this.poll = data['poll'];
      this.title = data['title'];
      this.url = data['url'];
      this.initForm(Object.keys(this.poll));
      console.log('Anketa po modelu: ', this.poll);
      console.log('Naslov lekcije: ', this.title);
      console.log('Url na koji se šalju podaci: ', this.url);
    });
  }
  
  initForm(keys: any) {
    console.log('initForm: ', keys);
    for (let key of keys) {
      console.log(key);
      this.pollForm.addControl(key, new FormControl('', Validators.required));
    }
    // this.pollForm.addControl('comment', new FormControl(''));
    console.log(this.pollForm);

  }

  sendData() {
    console.log("sendData funkcija");
    console.log("vrijednosti ankete: ", this.pollForm.value);
    //let req = this.http.post('https://webhook.site/59520929-b3a8-474b-a7d7-df5bd5661ccd', data, this.httpOptions);
    let req = this.http.post(this.url, this.pollForm.value);
    req.subscribe(
        res =>{
            console.log("Odgovor servera: ", res);
            this.serverResponse = res;
        },
        err => {
            console.log("Odjeb servera: ", err.message);
            this.serverResponse = err.message;
        }
      );
  }
  
  getPoll(): AnketaModel{
    return this.poll;
  }

  getTitle(): string{
    return this.title;
  }

  getServerResponse(): any{
    return this.serverResponse;
  }
}
