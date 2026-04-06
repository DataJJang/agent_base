using UnityEngine;

namespace SampleGame.Bootstrap
{
    public class GameBootstrap : MonoBehaviour
    {
        [SerializeField] private string projectName = "__PROJECT_NAME__";
        [SerializeField] private string projectPurpose = "__PROJECT_PURPOSE__";

        private void Start()
        {
            Debug.Log($"[bootstrap] {projectName} / {projectPurpose}");
        }
    }
}

