from client import AgenticHallucinationCrossExaminationDebateClient

def main():
    client = AgenticHallucinationCrossExaminationDebateClient()
    res = client.conduct_adversarial_cross_examination()
    print('Debate Cross-Examination: ' + res['audit_id'] + ' (' + res['verdict'] + ')')
    print('Robustness: ' + str(res['robustness_score']) + ' | Flags: ' + str(res['hallucination_flags_count']))
    print('Transcript URL: ' + res['debate_transcript_url'])

if __name__ == '__main__':
    main()
