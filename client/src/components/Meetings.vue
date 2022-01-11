<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Meeting Organizer</h1>
        <hr><br><br>
        <alert :message=message v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.meeting-modal>
        Toplanti Ekle</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Toplanti Konusu</th>
              <th scope="col">Tarih</th>
              <th scope="col">Baslangic Saati</th>
              <th scope="col">Bitis Saati</th>
              <th scope="col">Katilimcilar</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(meeting, index) in meetings" :key="index">
              <td>{{ meeting.subject }}</td>
              <td>{{ meeting.date }}</td>
              <td>{{ meeting.stime }}</td>
              <td>{{ meeting.ftime }}</td>
              <td>{{ meeting.subs }}</td>

              <td>
                <div class="btn-group" role="group">
                  <button
        type="button"
        class="btn btn-warning btn-sm"
        v-b-modal.meeting-update-modal
        @click="editMeeting(meeting)">
          Guncelle
        </button>
                  <button
        type="button"
        class="btn btn-danger btn-sm"
        @click="onDeleteMeeting(meeting)">
           Sil
            </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addMeetingModal"
         id="meeting-modal"
         title="Toplanti Kayit Formu"
         hide-footer>
  <b-form @submit="onSubmit" @reset="onReset" class="w-100">

  <b-form-group id="form-title-group"
                label="Toplanti Konusu:"
                label-for="form-title-input">
      <b-form-input id="form-title-input"
                    type="text"
                    v-model="addMeetingForm.subject"
                    required
                    placeholder="Konu Giriniz">
      </b-form-input>
    </b-form-group>

    <b-form-group id="form-author-group"
                  label="Tarih:"
                  label-for="form-author-input">
        <b-form-input id="form-author-input"
                      type="date"
                      v-model="addMeetingForm.date"
                      required
                      placeholder="Tarih Giriniz">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-group"
                  label="Baslangic Saati:"
                  label-for="form-author-input">
        <b-form-input id="form-author-input"
                      type="time"
                      v-model="addMeetingForm.stime"
                      required
                      placeholder="Saat Giriniz">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-group"
                  label="Bitis Saati:"
                  label-for="form-author-input">
        <b-form-input id="form-author-input"
                      type="time"
                      v-model="addMeetingForm.ftime"
                      required
                      placeholder="Saat Giriniz">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-group"
                  label="Katilimcilar:"
                  label-for="form-author-input">
      <b-form-tags input-id="tags-basic" v-model="addMeetingForm.subs"></b-form-tags>
      </b-form-group>

    <b-button type="submit" variant="primary">Ekle</b-button>
    <b-button type="reset" variant="danger">Vazgec</b-button>
  </b-form>
</b-modal>
<b-modal ref="editMeetingModal"
         id="meeting-update-modal"
         title="Toplanti Guncelleme Formu"
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
  <b-form-group id="form-title-edit-group"
                label="Toplanti Konusu:"
                label-for="form-title-edit-input">
      <b-form-input id="form-title-edit-input"
                    type="text"
                    v-model="editForm.subject"
                    required
                    placeholder="Konu Giriniz">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-author-edit-group"
                  label="Tarih:"
                  label-for="form-author-edit-input">
        <b-form-input id="form-author-edit-input"
                      type="date"
                      v-model="editForm.date"
                      required>
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-edit-group"
                  label="Baslangic Saati:"
                  label-for="form-author-edit-input">
        <b-form-input id="form-author-edit-input"
                      type="time"
                      v-model="editForm.stime"
                      required>

        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-edit-group"
                  label="Bitis Saati:"
                  label-for="form-author-edit-input">
        <b-form-input id="form-author-edit-input"
                      type="time"
                      v-model="editForm.ftime"
                      required>
        </b-form-input>
      </b-form-group>
       <b-form-group id="form-author-group"
                  label="Katilimcilar:"
                  label-for="form-author-input">
      <b-form-tags input-id="tags-basic" v-model="editForm.subs"></b-form-tags>
      </b-form-group>

    <b-button-group>
      <b-button type="submit" variant="primary">Guncelle</b-button>
      <b-button type="reset" variant="danger">Vazgec</b-button>
    </b-button-group>
  </b-form>
</b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      meetings: [],
      addMeetingForm: {
        subject: '',
        date: '',
        stime: '',
        ftime: '',
        subs: [],

      },
      editForm: {
        id: '',
        subject: '',
        date: '',
        stime: '',
        ftime: '',
        subs: [],

      },
      message: '',
      showMessage: false,

    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getMeetings() {
      const path = 'http://localhost:5000/meetings';
      axios.get(path)
        .then((res) => {
          this.meetings = res.data.meetings;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addMeeting(payload) {
      const path = 'http://localhost:5000/meetings';
      axios.post(path, payload)
        .then(() => {
          this.getMeetings();
          this.message = 'Toplanti Eklendi!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getMeetings();
        });
    },
    initForm() {
      this.addMeetingForm.subject = '';
      this.addMeetingForm.date = '';
      this.addMeetingForm.stime = '';
      this.addMeetingForm.ftime = '';
      this.addMeetingForm.subs = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addMeetingModal.hide();
      const payload = {
        subject: this.addMeetingForm.subject,
        date: this.addMeetingForm.date,
        stime: this.addMeetingForm.stime,
        ftime: this.addMeetingForm.ftime,
        subs: this.addMeetingForm.subs,

      };
      this.addMeeting(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addMeetingModal.hide();
      this.initForm();
    },
    editMeeting(meeting) {
      this.editForm = meeting;
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editMeetingModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        subject: this.editForm.subject,
        date: this.editForm.date,
        stime: this.editForm.stime,
        ftime: this.editForm.ftime,
        subs: this.editForm.subs,
        read,
      };
      this.updateMeeting(payload, this.editForm.id);
    },
    updateMeeting(payload, meetingID) {
      const path = `http://localhost:5000/meetings/${meetingID}`;
      axios.put(path, payload)
        .then(() => {
          this.getMeetings();
          this.message = 'Toplanti Guncellendi!';
          this.showMessage = true;
        })
        .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
          this.getMeetings();
        });
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editMeetingModal.hide();
      this.initForm();
      this.getMeetings(); // why?
    },
    removeMeeting(meetingID) {
      const path = `http://localhost:5000/meetings/${meetingID}`;
      axios.delete(path)
        .then(() => {
          this.getMeetings();
          this.message = 'Toplanti Silindi!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getMeetings();
        });
    },
    onDeleteMeeting(meeting) {
      this.removeMeeting(meeting.id);
    },
  },
  created() {
    this.getMeetings();
  },
};
</script>
