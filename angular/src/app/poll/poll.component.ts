import { Component, OnInit } from '@angular/core';
import { FormGroup, FormBuilder, FormControl, Validators } from '@angular/forms';
import { OdgovorModel } from '../models/odgovor.model';
import { ActivatedRoute, Router } from '@angular/router';
import { DataService } from '../services/data.service';

@Component({
  selector: 'app-poll',
  templateUrl: './poll.component.html',
  styleUrls: ['./poll.component.css']
})
export class PollComponent implements OnInit {
  lekcija: string;
  pollForm = new FormGroup({});
  odgovor: OdgovorModel;
  anketa: any;

  constructor(private route: ActivatedRoute,
              private router: Router,
              private dataService: DataService,
              private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.dataService.parseData();
    // this.pollForm.addControl('comment', new FormControl(''));
    // this.initForm(Object.keys(this.dataService.getPoll()));
    // this.dataService.getTemplate().subscribe(data => {
    //   this.anketa = data['anketa'];
    //   this.lekcija = data['naslov'];
    //   console.log("Ključevi ankete: ", Object.keys(this.anketa));
    //   console.log("Podaci ankete: ", this.anketa);
    //   console.log("Naslov lekcije: ", this.lekcija);
    //   // this.pollForm = new FormGroup({});
    //   this.initForm(Object.keys(this.anketa));
    //   this.pollForm.addControl('comment', new FormControl(''));
    // });
  }

  initForm(keys: any) {
    // this.pollForm = new FormGroup({});
    console.log('initForm: ', keys);
    for (let key of keys) {
      console.log(key);
      this.pollForm.addControl(key, new FormControl('', Validators.required));
    }
    // this.pollForm.addControl('comment', new FormControl(''));
    console.log(this.pollForm);

  }

  onSubmit() {
    console.log(this.pollForm.value);
	  this.dataService.sendData();
    this.router.navigate(['/success']);
  }

}
