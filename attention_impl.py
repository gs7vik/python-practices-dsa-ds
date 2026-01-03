import torch
import torch.nn as nn
import math

class SingleHeadAttention(nn.Module):
    def __init__(self,d_model):
        
        """
       d_model is the dimension of input embeddings(100,768)
       
        """
        
        super().__init__()
        self.d_model = d_model
        
        #1. Define linear projections of Q,K,V
        #this creates weight matrices for Q,K,V each of shape (d_model, d_model)
        
        self.w_q = nn.Linear(in_features=d_model, out_features=d_model, bias=False)
        print(self.w_q.weight.shape)
        self.w_k = nn.Linear(in_features=d_model, out_features=d_model, bias=False)
        self.w_v = nn.Linear(in_features=d_model, out_features=d_model, bias=False)
        
        self.out_proj = nn.Linear(in_features=d_model, out_features=d_model)
        
        
    def forward(self, x, mask=None):
        """
        Docstring for forward
        
        :param self: Description
        :param x: input embedding of shape(batch_size, seq_len, d_model)
        :param mask: Description(optional mask for decoder )
        """ 
        
        B,T,D = x.shape
        #B indicates batch size(neural networks process batch of sentences in parallel to speed up things), if you feed 32 diff sentences at once then b=32
        #T represents sequence length(or number of tokens in the sentence) I love coding, here if each word is a token then there are 3 tokens T = 4
        #D represents the dimension or embedding size
        
        #2. Project input to Q,K,V
        Q = self.w_q(x)
        K = self.w_k(x)
        V = self.w_v(x)
        
        #3. Compute Attention scores(Scaled dot product of Q and K)
        # Q: [B, T, D]
        # K_transpose: [B, D, T] (Transpose the last two dimensions)
        # Result (scores): [B, T, T] -> relationships between every token and every other token
        #Why do we transpose?
        #Matrix Q: shape [T,D]
        #Matrix K: shape[T,D]
        
        #rule of mat mul: inner dimension must match (row*col).(row*col)
        #if we try to directly multiply Q and K then we get (4*512).(4*512) so for this reason we transpose
        #when we apply transpose K becomes (512, 4)
        #here -2,-1 indicates last two dimensions, basically saying swap the second to last dimension with the last dimension
        scores = torch.matmul(Q,K.transpose(-2,-1))

        #Scale the scores to prevent vanishing gradients in softmax
        scores = scores/ math.sqrt(D)
        
        
        #4. Apply Masking(optional, but needed for Decoder)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
            
        #5. Apply softmax to get prob
        #Shape: [B,T,T]
        #Shape: [Batch, Query_Len (T), Key_Len (T)]
        #for each word(query) we want to find how much it focuses on all other words(keys), so we use the last dimension (-1)
        attention_weights = torch.softmax(scores, dim=-1)
        
        
        #6. Multiply weights by values 
        # weights: [B, T, T] @ V: [B, T, D] -> [B, T, D]
        context = torch.matmul(attention_weights, V)
        
        #7. final op projection
        output = self.out_proj(context)
        
        return output, attention_weights
    
    
if __name__ == "__main__":
    
    batch_size = 2
    seq_len = 5
    d_model = 64
    
    #create random input 
    input_embeddings = torch.randn(batch_size, seq_len, d_model)
    
    attention_layer = SingleHeadAttention(d_model)
    
    #forward pass
    output, weights = attention_layer(input_embeddings)
    print("Sum of weights:",weights[0, 0, :].sum())
    print(f"Input Shape:  {input_embeddings.shape}")
    print(f"Output Shape: {output.shape}")
    
        