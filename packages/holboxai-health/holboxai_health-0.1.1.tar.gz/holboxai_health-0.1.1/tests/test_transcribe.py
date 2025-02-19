import unittest
from unittest import mock

from holboxai_health import transcribe_audio


class FakeS3Client:
    def upload_file(self, audio_file, s3_bucket, s3_key):
        self.upload_file_called = True
        self.upload_file_params = (audio_file, s3_bucket, s3_key)


class FakeTranscribeClient:
    def __init__(self):
        self.transcription_kwargs = None

    def start_medical_transcription_job(self, **kwargs):
        self.transcription_kwargs = kwargs

    def get_medical_transcription_job(self, MedicalTranscriptionJobName):
        return {
            "MedicalTranscriptionJob": {
                "TranscriptionJobStatus": "COMPLETED",
                "Transcript": {
                    "TranscriptFileUri": "http://dummy_url"
                }
            }
        }


class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {"Summary": "This is a fake summary."}


class TestTranscribeAudio(unittest.TestCase):
    @mock.patch('boto3.client')
    @mock.patch('healthscribe.aws_auth.get_transcribe_client')
    @mock.patch('requests.get')
    @mock.patch('time.sleep', return_value=None)
    def test_transcribe_audio_success(self, sleep_mock, requests_get_mock, get_transcribe_client_mock, boto3_client_mock):
        fake_s3_client = FakeS3Client()
        boto3_client_mock.return_value = fake_s3_client

        fake_transcribe_client = FakeTranscribeClient()
        get_transcribe_client_mock.return_value = fake_transcribe_client

        requests_get_mock.return_value = FakeResponse()

        summary = transcribe_audio("dummy_audio.wav", "testJob", "dummyBucket", "dummyKey")

        self.assertEqual(summary, "This is a fake summary.")
        self.assertTrue(hasattr(fake_s3_client, "upload_file_called"))
        self.assertIsNotNone(fake_transcribe_client.transcription_kwargs)
        self.assertEqual(fake_transcribe_client.transcription_kwargs.get("MedicalTranscriptionJobName"), "testJob")


if __name__ == '__main__':
    unittest.main()
